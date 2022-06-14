import email
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class InstitutionData(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    tel=models.CharField(unique=True,max_length=255)
    institution_tin=models.CharField(max_length=255,unique=True)
    INSTITUTION_TYPE = (
        ('DRIVING_SCHOOL', 'DRIVING SCHOOL'),
        ('HIGH_SCHOOL', 'HIGH SCHOOL'),        
    )
    institution_type = models.CharField(max_length=255, blank=False, choices=INSTITUTION_TYPE,)

    def __str__(self):
        return self.name
class User(AbstractUser):
    instituon_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(unique=True,max_length=255)
    password=models.CharField(max_length=255)
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.name