from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    face_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    marked = models.BooleanField(default=False)
