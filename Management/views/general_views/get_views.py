from datetime import datetime
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializer.general_serializer.serializers import DepartmentSerializer, EmployeeSerializer,JobTitleSerializer,UserSerializer,InstitutionSerializer
from rest_framework.response import Response
from ...models import User
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime,requests
from rest_framework import permissions, exceptions
from ...system_module.general_models.models import InstitutionDepartment,InstitutionData,InstitutionEmployee,InstitutionJobTitle


class GetInstitutionView(APIView):
    def get(self,request):
        institution=InstitutionData.objects.all()
        serializer=InstitutionSerializer(institution,many=True)
        return Response(serializer.data)

class GetDepartmentView(APIView):
    def get(self,request):
        departmets=InstitutionDepartment.objects.all()
        serializer=DepartmentSerializer(departmets,many=True)
        return Response(serializer.data)

class GetJobTititletView(APIView):
    def get(self,request):
        jobs=InstitutionJobTitle.objects.all()
        serializer=JobTitleSerializer(jobs,many=True)
        return Response(serializer.data)

class GetEmployeeView(APIView):
    def get(self,request):
        employees=InstitutionEmployee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

class GetUserView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)