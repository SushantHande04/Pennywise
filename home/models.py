from django.db import models
from django.contrib.auth.models import User

class addcash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique = False)
    purpose = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=8, decimal_places=0)
    date = models.DateField()

    '''def __str__(self):
        username = self.user.username
        return username'''

class user_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique = False)
    income = models.DecimalField(max_digits=8, decimal_places=0,  default=0)