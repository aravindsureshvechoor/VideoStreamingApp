from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import UserRegistrationView,UserLoginView

class TestUrls(SimpleTestCase):

    # this functions tests if the URL's are correctly mapping to the recommended views

    def test_user_signup(self):
        url = reverse('user_signup')
        self.assertEquals(resolve(url).func.view_class, UserRegistrationView)

    def test_user_login(self):
        url = reverse('user_login')
        self.assertEquals(resolve(url).func.view_class, UserLoginView)

    