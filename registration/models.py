from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
   
    email = models.EmailField("user email", unique=True)
    passwd = models.CharField("user password", max_length=200)
    #name = models.CharField("full name", max_length=500)
    #creation_date = models.DateTimeField("date user cretaed", auto_now_add=True)
    #last_login  = models.DateTimeField("date last login")
    #login_count = models.IntegerField(default=0)
    
    #this tells django which is the unique field here, by default it is username 
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user_email

