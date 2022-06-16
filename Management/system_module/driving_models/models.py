import email
from statistics import mode
from tkinter import CASCADE
from django.db.models.signals import pre_save
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from ...utils.utils import unique_new_code_generator
from ..general_models.models import InstitutionData



class CourseData(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=25,primary_key=True)
    description=models.CharField(max_length=255,help_text="What the course Entails")
    total_payable=models.IntegerField(help_text="Total amount of the course")
    institution_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=CourseData)
class NtsaCharges(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=25,primary_key=True)
    amount=models.IntegerField(help_text="Prices Per NTSA Charge")
    def __str__(self):
        return self.name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=CourseData)
# class AdmissionStudent(models.Model):
#     full_name=models.CharField(max_length=255)
#     national_id=models.CharField(max_length=255)
#     kra_pin=models.CharField(max_length=255)
#     has_tims_account=models.BooleanField(default=False,help_text="If the Have NTSA account")
#     national_id=models.CharField(max_length=255)
#     institution_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)