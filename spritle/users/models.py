from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.
class StreamUser(AbstractBaseUser):
    first_name        = models.CharField(max_length=50)
    last_name         = models.CharField(max_length=50)
    user_name         = models.CharField(max_length=50,unique=True)
    email             = models.EmailField(max_length=254,unique=True)
    password          = models.CharField(max_length=50)
    is_admin          = models.BooleanField(default=False)
    is_staff          = models.BooleanField(default=False)
    is_superuser      = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    
    USERNAME_FIELD    = 'email'
    REQUIRED_FIELDS   = ['user_name','first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name},id->{self.id}"

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,add_label):
        return True
