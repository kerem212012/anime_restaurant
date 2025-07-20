from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True,verbose_name="Username")
    first_name = models.CharField(max_length=50,verbose_name="First Name")
    last_name = models.CharField(max_length=50,verbose_name="Last Name")
    phone_number = PhoneNumberField(verbose_name="Phone Number")
    email = models.EmailField(max_length=50, unique=True, blank=True,verbose_name="E-mail")
    picture = models.ImageField(blank=True, verbose_name="Picture",upload_to="user_pictures", default="user_pictures/default.png")  # TODO make default
    email_verifed=models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
