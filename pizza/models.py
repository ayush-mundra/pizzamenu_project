from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
   pizza_type = models.CharField(max_length=200, default="regular")
   pizza_size = models.CharField(max_length=200,default='small size')
   pizza_topping = models.CharField(max_length=20, default="onion")
   owner = models.ForeignKey(User, on_delete=models.CASCADE)


