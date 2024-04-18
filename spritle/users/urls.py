from django.urls import path
from .views import (UserRegistrationView,UserLoginView)

urlpatterns = [
    path('usersignup/',UserRegistrationView.as_view(),name='user_signup'),
    path('userlogin/',UserLoginView.as_view(),name='user_login'),
]