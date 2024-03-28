
from dataclasses import field
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager,User

# Create your models here.
# this will store the user details in an abstract class
class UserManager(BaseUserManager):
    def create_user(self, name, email, password):
        user = self.model(name=name, email=email, username=email.split("@")[0],password=password)
        user.set_password(password)
        user.save(using=self._db)
        print("User Created",user.name,user.email,user.username)
        return user

class User(AbstractBaseUser):
    name = models.CharField(db_column='Name', max_length=35)
    email = models.CharField(db_column='Email', max_length=100, primary_key=True)
    username = models.CharField(db_column='Username', max_length=100)
    password = models.CharField(db_column='Password', max_length=100)
    

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Course(models.Model):
    name = models.CharField(max_length = 30, null = True)
    slug = models.CharField(max_length = 50, null = False, unique=True)
    description = models.CharField(max_length = 200, null = True)
    days = models.CharField(max_length=30, null = True)
    price = models.CharField(max_length = 50, null = True)
    thumbnail = models.ImageField(upload_to = "files/thumbnail", null=True)
    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    class Meta : 
        abstract = True


class Tag(CourseProperty):
    pass
    
class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length = 100, null = True)
    course = models.ForeignKey(Course , null = False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null = True)
    video_id = models.CharField(max_length=100, null = True)
    is_preview = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Schedule(models.Model):
    name = models.CharField(max_length = 30, null = True)
    slug = models.CharField(max_length = 50, null = False, unique=True)
    description = models.CharField(max_length = 200, null = True)
    days = models.CharField(max_length = 30, null = True)
    timing = models.CharField(max_length = 30, null = True)
    trainer = models.CharField(max_length = 30, null = True)
    phno = models.CharField(max_length=20, null = True, unique=True)
    mailid = models.CharField(max_length=100, null=True, unique=True)
    thumbnail = models.ImageField(upload_to = "files/thumbnail", null=True)
    def __str__(self):
        return self.name

# this will store user details in database
# class UserInfo(models.Model):
#     name = models.CharField(db_column='Name', max_length=35)
#     email = models.CharField(db_column='Email', max_length=100, primary_key=True)
