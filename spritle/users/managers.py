from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,first_name,last_name,user_name,email,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not user_name:
            raise ValueError('User must have a username')

        user = self.model(
            email       = self.normalize_email(email),
            user_name   = user_name,
            first_name  = first_name,
            last_name   = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,first_name,last_name,email,user_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
