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


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    P_price = models.FloatField()
    description = models.TextField(max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    pic = models.ImageField(upload_to="productPic", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)
