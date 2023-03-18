from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password= None): 
        if not email:
            raise ValueError('El usuario debe tener un correo')


        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(
            email = self.normalize_email(email), username = username,
            first_name = first_name, last_name = last_name,
        ) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user


