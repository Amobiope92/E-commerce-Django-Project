from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

position = [
        ('HR', 'HR'),
        ('Accountant', 'Accountant'),
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('Customer_care', 'Customer_care'),
    ]

state = [
        ('Oyo', 'Oyo'),
        ('Osun', 'Osun'),
        ('Ogun', 'Ogun'),
        ('Lagos', 'Lagos'),
    ]

marital_status = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Complicated', 'Complicated'),
    ]

class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    position = models.CharField(choices = position, unique= False, max_length= 20)
    state = models.CharField(choices = state, unique= False, max_length= 20)
    marital_status = models.CharField(choices = marital_status, unique= False, max_length= 20)
    Phone_number = models.CharField(max_length= 11, unique= True)
    


product_category=[
                  ('Electronics', 'Electronics'),
                  ('Wears', 'Wears'),
                  ('Lotions', 'Lotions'),
                  ('Gym kits', 'Gym Kits'),

]

# class User(models.Model):


class product(models.Model):
    product_id = models.IntegerField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    category= models.CharField(choices= product_category, unique=False, max_length=30)
    quantity= models.IntegerField()
    price= models.CharField(max_length=30)
    description= models.CharField(max_length=50)        
