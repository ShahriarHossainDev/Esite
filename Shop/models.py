from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userProfile(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'female'),
        ('Other', 'Other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=Gender)
    image = models.ImageField(upload_to='profilePic')
    birthday = models.DateTimeField(null=True)
    phone_number = models.IntegerField()
    address = models.TextField(max_length=200, default='Add Your Address')

    def __str__(self):
        return str(self.user)
