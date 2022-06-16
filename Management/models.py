import email
from statistics import mode
from tkinter import CASCADE
from django.db.models.signals import pre_save
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils.utils import unique_new_code_generator
from .system_module.general_models.models import InstitutionData

class User(AbstractUser):
    institution_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255,primary_key=True)
    email=models.CharField(unique=True,max_length=255)
    password=models.CharField(max_length=255)
    username=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=User)
