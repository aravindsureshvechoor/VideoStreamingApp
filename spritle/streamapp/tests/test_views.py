from django.test import TestCase,Client
from streamapp.serializers import *
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
import json,os



User = get_user_model()



# this class is responsible for running and ensuring all the views in the streamapp is working accordingly
class TestStreamingAppViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(

                    first_name       = 'user_firstname1',
                    last_name        = 'user_lastname1',
                    user_name        = 'user_username1',
                    email            = 'user@example1.com',
                    password         = 'userpassword',

                                           )
        self.client = Client()





    # here we are letting a sample user authenticate,since all the views check the identity first before execution
    def authenticate_user(self):

        test_user  = User.objects.create_user(

                    first_name       = 'user_firstname',
                    last_name        = 'user_lastname',
                    user_name        = 'user_username',
                    email            = 'user@example.com',
                    password         = 'userpassword',

                                           )

        login_data  = {
                'email'   :'user@example.com',
                'password':'userpassword'
                     }

        url         = reverse('user_login')

        response    = self.client.post(url,data=login_data,format='json')

        self.assertEqual(response.status_code,200)
        self.assertIn('access and refresh tokens', response.data)

        access_token = response.data['access and refresh tokens']['access'] 

        return access_token






    # this function checks if the video is uploading successfully with the status code 201_CREATED
    def test_upload_video_view_success(self):

        access_token     = self.authenticate_user()

        headers          = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        url              = reverse('upload_video')

        # Get the absolute path to the video file within the Django project directory
        video_path       = "/home/aravind/Desktop/Video Streaming APP/media_root/videos/2024/04/17/Batman_Social_Media.webm"

        # ADD AN EXISTING FILE IN THE LOCAL MACHINE FOR THE CORRECT FUNCTIONALITY
        if os.path.exists(video_path):
            with open(video_path, 'rb') as video_file:
                response = self.client.post(url, {'streamer': 1, 'title': 'Test Video', 'video_URL': SimpleUploadedFile('Batman_Social_Media_CORdo10.webm', video_file.read())}, format='multipart/form-data', **headers)
            self.assertEqual(response.status_code,201)
        else:
            print(f"Error: Video file not found at '{video_path}'")





    
    # this function checks if the view is correctly responding to errors with the status code 400
    def test_upload_video_view_failure(self):

        access_token     = self.authenticate_user()

        headers          = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        url              = reverse('upload_video')

        # Get the absolute path to the video file within the local machine
        video_path       = "/home/aravind/Desktop/Video Streaming APP/media_root/videos/2024/04/17/Batman_Social_Media.webm"


        # ADD AN EXISTING FILE IN THE LOCAL MACHINE FOR THE CORRECT FUNCTIONALITY
        if os.path.exists(video_path):
            with open(video_path, 'rb') as video_file:
                response = self.client.post(url, { 'title': 'Test Video', 'video_URL': SimpleUploadedFile('Batman_Social_Media_CORdo10.webm', video_file.read())}, format='multipart/form-data', **headers)
            self.assertEqual(response.status_code,400)
        else:
            print(f"Error: Video file not found at '{video_path}'")






    # this testcase checks if the PlayVideoView is successfully playing the video
    @patch('streamapp.video_player')
    def test_play_video_success(self,mock_video_player):

        access_token  = self.authenticate_user()

        headers       = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        video_path    = "/home/aravind/Desktop/Video Streaming APP/media_root/videos/2024/04/17/Batman_Social_Media.webm"

        video         = Video.objects.create(streamer=self.user,title='Test Video', video_URL='path/to/test_video.mp4')

        # Mock the VideoPlayer class and its play_video method
        mock_instance = mock_video_player.return_value
        mock_instance.play_video.return_value = None

        # Make a POST request to the PlayVideoView
        url           = reverse('play_video', kwargs={'video_id': video.id})
        response      = self.client.post(url,**headers)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)





    # this test case checks if the UpdateVideoView is working successfully with a status code of 200
    def test_update_video_success(self):

        access_token = self.authenticate_user()

        headers      = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        video        = Video.objects.create(streamer=self.user,title='Test Video', video_URL='path/to/test_video.mp4')

        url          = reverse('update_video',kwargs={'video_id':video.id})
     
        data         = {'title': 'Updated Title'}  # Your updated data
        response     = self.client.put(url, data,**headers, content_type='application/json') 
        self.assertEqual(response.status_code,200)



    # this test case checks if the DestroyVideoView can successfully delete an existing video
    def test_delete_video(self):

        access_token = self.authenticate_user()

        headers      = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        video        = Video.objects.create(streamer=self.user,title='Test Video', video_URL='path/to/test_video.mp4')

        url          = reverse('delete_video',kwargs={'id':video.id})

        response     = self.client.delete(url,**headers)

        self.assertEqual(response.status_code,204)



    # this unit test function checks if the SearchVideoView is working successfully and responding with statuscode 200
    def test_search_functionality_success(self):

        access_token = self.authenticate_user()

        headers      = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        video        = Video.objects.create(streamer=self.user,title='Test Video', video_URL='path/to/test_video.mp4')

        query = 'Test'

        url = reverse('search_video') + f'?search_query={query}'

        response     = self.client.get(url,**headers)

        self.assertEqual(response.status_code,200)



    # this testcase checks if the FetchAllVideosView is working successfully with the status code 200_OK
    def test_fetch_all_videos(self):

        access_token = self.authenticate_user()

        headers      = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}

        url          = reverse('fetch_all_videos')

        response     = self.client.get(url,**headers)

        self.assertEqual(response.status_code,200)




# UNIT TESTS FOR ALL VIEWS IN THE 'streamapp' ENDS HERE
    







        