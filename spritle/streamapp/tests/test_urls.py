from django.test import SimpleTestCase
from django.urls import reverse,resolve
from streamapp.views import (UploadVideoView,PlayVideoView,UpdateVideoView,DestroyVideoView,SearchVideoView,FetchAllVideosView)



class TestUrls(SimpleTestCase):

    # this functions tests if the URL's are correctly mapping to the recommended views


    def test_upload_video_url_is_resolved(self):
        url = reverse('upload_video')
        self.assertEquals(resolve(url).func.view_class, UploadVideoView)


    def test_play_video_url_is_resolved(self):
        id_value = 1
        url      = reverse('play_video',kwargs={'video_id':id_value})
        self.assertEquals(resolve(url).func.view_class, PlayVideoView)


    def test_update_video_url_is_resolved(self):
        id_value = 1
        url      = reverse('update_video',kwargs={'video_id':id_value})
        self.assertEquals(resolve(url).func.view_class, UpdateVideoView)


    def test_delete_video_url_is_resolved(self):
        id_value = 1
        url      = reverse('delete_video',kwargs={'id':id_value})
        self.assertEquals(resolve(url).func.view_class, DestroyVideoView)


    def test_search_video_url_is_resolved(self):
        id_value = 1
        url      = reverse('search_video')
        self.assertEquals(resolve(url).func.view_class, SearchVideoView)


    def test_fetch_all_videos_url_is_resolved(self):
        url = reverse('fetch_all_videos')
        self.assertEquals(resolve(url).func.view_class, FetchAllVideosView)

   

