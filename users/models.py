from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin


# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
       
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password=None , **kwargs):
       
        user = self.create_user(
            email,
            password=password,
            **kwargs 
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class UserAccount(AbstractBaseUser , PermissionsMixin):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    artistname= models.CharField(max_length=255 , unique=True , blank=True , null=True)

    email = models.EmailField(unique=True , max_length=255)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        upload_to='images/',
        null=True)
    background = models.ImageField(
        upload_to='images/',
        null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()
    
    def get_image(self):
        if self.profile_pic:
            return 'http://127.0.0.1:8000' + self.profile_pic.url
        return ''
    
    def get_background(self):
         if self.background:
            return 'http://127.0.0.1:8000' + self.background.url
         return ''

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
