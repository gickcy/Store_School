
from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    wikipedia_link = models.URLField()


class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Purpose(models.Model):
    name = models.CharField(max_length=255)


class Material(models.Model):
    name = models.CharField(max_length=255)

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department_choices = [
        ('select your department', 'Select your department'),
        ('Degree', 'Degree'),
        ('Computer science','Computer Science'),
        ('Finance','Finance'),
    ]
    department = models.CharField(max_length=100,choices=department_choices)

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()


class UserCreation(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


class Authentication(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


