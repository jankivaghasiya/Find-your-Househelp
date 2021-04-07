from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class Works(models.Model):
    brooming = models.BooleanField(default='False')
    mopping = models.BooleanField(default='True')
    utensil_cleaning = models.BooleanField(default='False')
    washing_clothes = models.BooleanField(default='False')
    cooking = models.BooleanField(default='False')
    babysitting = models.BooleanField(default='False')

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.TextField()
    
class Helper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=50, default='')
    dob = models.DateField()
    years_of_experience = models.IntegerField(default=2)
    religion = models.CharField(max_length=50, default="")
    works = models.OneToOneField(Works, on_delete=models.CASCADE)

class Booking(models.Model):
    cutomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE)
    brooming = models.BooleanField(default='false')
    mopping = models.BooleanField(default='false')
    utensil_cleaning = models.BooleanField(default='false')
    washing_clothes = models.BooleanField(default='false')
    cooking = models.BooleanField(default='false')
    babysitting = models.BooleanField(default='false')