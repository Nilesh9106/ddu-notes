from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class College(models.Model):
    domain = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo/')
    def __str__(self):
        return self.name



NOTE_VISIBILITY_CHOICES = [
        ('1', 'Private'),
        ('2', 'College'),
        ('3', 'Public'),
]
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    college = models.ForeignKey(College,on_delete=models.SET_NULL,null=True)
    profilePic =models.ImageField(upload_to='profile/',default='/profile/default1.png')

    def __str__(self):
        return self.user.username
class Note(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    visibility = models.CharField(max_length=1,choices=NOTE_VISIBILITY_CHOICES,default='3')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    document = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title
    






