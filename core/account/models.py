from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,email,password,**extra_fields):
        """
        create and save a new user in database with email
        """
        if not email:
            raise ValueError(_("you need to set correct email"))
        email = self.normalize_email(email)
        user =self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        User.objects.create_user(user=user)
        return user
    
    def create_superuser(self,email,password):
        email = self.normalize_email(email)
        user =self.create_user(email = email,password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using =self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    """
    this is a custom model for create new user
    """
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email  
    
