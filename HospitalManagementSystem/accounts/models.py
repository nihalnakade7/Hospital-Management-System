from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyUsers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=50,default='None')

    def __str__(self):
        return self.user.first_name