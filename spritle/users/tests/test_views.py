from django.test import TestCase,Client
from users.serializers import *
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
User = get_user_model()


# this class checks the genuinity of the UserRegistrationView 
class TestUserRegistrationView(TestCase):

    def setUp(self):
        self.client            = Client()

    # this function checks if the userregistration works properly with the correct credentials
    def test_user_registration_success(self):
        user_data = {
            'first_name'       :'user_firstname',
            'last_name'        : 'user_lastname',
            'user_name'        : 'user_username',
            'email'            : 'user@example.com',
            'password'         : 'userpassword',
            'confirm_password' : 'userpassword'
        }

        serialized_data = UserRegistrationSerializer(data=user_data)

        self.assertTrue(serialized_data.is_valid())

        url             = reverse('user_signup')

        response        = self.client.post(url,data=user_data,format='json')

        self.assertEqual(response.status_code,201)


    # in this function we deliberately remove the username field to see if the view is passing correct error message
    def test_user_registration_failure(self):
        user_data = {
            'first_name'       :'user_firstname',
            'last_name'        : 'user_lastname',
            'email'            : 'user@example.com',
            'password'         : 'userpassword',
            'confirm_password' : 'userpassword'
        }

        serialized_data        = UserRegistrationSerializer(data=user_data)

        self.assertFalse(serialized_data.is_valid())

        url                    = reverse('user_signup')

        response               = self.client.post(url,data=user_data,format='json')

        self.assertEqual(response.status_code,400)









# this class checks the genuinity of the UserLoginView
class TestUserLoginView(TestCase):
    
    def setUp(self):
        self.client = Client()

    # this testcase checks if the UserLoginView authenticates user with the correct credentials
    def test_user_login_success(self):

        test_user   = User.objects.create_user(

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
    


    # this testcase checks if the view acts accordingly with response to invalid credentials
    def test_user_login_success(self):

        test_user   = User.objects.create_user(

                    first_name       = 'user_firstname',
                    last_name        = 'user_lastname',
                    user_name        = 'user_username',
                    email            = 'user@example.com',
                    password         = 'userpassword',

                                           )

        login_data = {
                'email'   :'user@example.com',
                'password':'wrongpassword'
                     }

        url        = reverse('user_login')

        response   = self.client.post(url,data=login_data,format='json')

        self.assertEqual(response.status_code,401)


    

