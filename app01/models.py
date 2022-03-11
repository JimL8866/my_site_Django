from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class UserDepartment(models.Model):
    section = models.CharField(max_length=50)


# class Title(models.Model):
#     title_name = models.CharField(max_length=30)
#     title_number = models.IntegerField()
