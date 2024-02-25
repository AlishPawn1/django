from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin, )
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def  create_user(self, email, username, password=None):
        if not username:
            raise ValueError('Username is a required field')
        if not email:
            raise ValueError('Email address is a required field')
        user = self.model(
            username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email, username, password = None ):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField("username", null = False, blank = False,)
    email = models.EmailField(
        "Email Address", 
        unique = True,
        primary_key = True,
    )
    is_admin = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    objects = UserManager()
    
    @property
    def is_staff(self):
        return self.is_admin 