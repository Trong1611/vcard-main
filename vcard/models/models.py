from typing import Any
from django.db import models
from django.conf import settings


class Users(models.Model):
    UserID = models.CharField(max_length=50, unique=True)
    UserName = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=15)


class VcardInformation(models.Model):
    class Meta:
        db_table="vcard_information"
    UserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")
    DisplayName = models.CharField(max_length=200, db_column="display_name")
    Company = models.CharField(max_length=200, db_column="company")
    Position = models.CharField(max_length=200, db_column="position")
    PhoneNumber = models.CharField(max_length=12, db_column="phone_number")
    Address = models.CharField(max_length=200, db_column="address")
    Email = models.CharField(max_length=50, db_column="email")
    Website = models.CharField(max_length=50, db_column="website")
    fileName = models.CharField(max_length=100, db_column="file_name")
    template = models.IntegerField(db_column="template", default=0)
    logo = models.CharField(max_length=100, db_column="logo", default="")
    active = models.BooleanField(default=True, db_column="active")


class UserInformation(models.Model):
    UserID = models.CharField(max_length=50, unique=True)
    DisplayName = models.CharField(max_length=200)
    Company = models.CharField(max_length=200)
    Position = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=12)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Website = models.CharField(max_length=50)


class UserQRLocation(models.Model):
    UserID = models.CharField(max_length=50)
    QRPath = models.CharField(max_length=1000)


# Create your models here.
