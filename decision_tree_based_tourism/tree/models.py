from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username
    
class Package(models.Model):
    name = models.CharField(max_length=20,null=True)
    image1 = models.FileField(null=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    description = models.CharField(max_length=100,null=True)
    price = models.IntegerField(max_length=50,null=True)
    duration = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    packageType = models.CharField(max_length=20,null=True)



class Review(models.Model):
    packageID = models.CharField(max_length=20,null=True)
    packagename = models.CharField(max_length=20,null=True)
    userName = models.CharField(max_length=20,null=True)
    review = models.CharField(max_length=20,null=True)
    rating = models.CharField(max_length=20,null=True)


class Booking(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    number = models.CharField(max_length=20,null=True)
    packageID = models.CharField(max_length=20,null=True)
    packagename = models.CharField(max_length=20,null=True)
    count = models.CharField(max_length=20,null=True)
    date = models.CharField(max_length=20,null=True)
    type = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    amount = models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=20,null=True)

