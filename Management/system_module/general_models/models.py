import email
from statistics import mode
from tkinter import CASCADE
from django.db.models.signals import pre_save
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from ...utils.utils import unique_new_code_generator

# Create your models here.
class InstitutionData(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255,primary_key=True)
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
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=InstitutionData)
class InstitutionDepartment(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255,primary_key=True)
    institution_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=InstitutionDepartment)
class InstitutionJobTitle(models.Model):
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255,primary_key=True)
    department_code=models.ForeignKey(InstitutionDepartment,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=InstitutionJobTitle)
class InstitutionEmployee(models.Model):
    institution_code=models.ForeignKey(InstitutionData,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    code=models.CharField(max_length=255,primary_key=True)
    last_name=models.CharField(max_length=255)
    national_id=models.CharField(max_length=255)
    kra_pin=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    is_user = models.BooleanField(default=False)
    email=models.EmailField(max_length=255,unique=True)
    job_title_code=models.ForeignKey(InstitutionJobTitle,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
def pre_save_create_course_code(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code=unique_new_code_generator(instance)
pre_save.connect(pre_save_create_course_code,sender=InstitutionEmployee)

