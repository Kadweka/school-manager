from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer.serializers import DepartmentSerializer, EmployeeSerializer,JobTitleSerializer,UserSerializer,InstitutionSerializer
from rest_framework.response import Response
import requests
# Create your views here.
url='http://localhost:8000/register'
class HellowView(APIView):
    def get(self,request):
        content={'message':'Hellow World'}
        return Response(content)
class InstitutionView(APIView):
    def post(self,request):
        serializer=InstitutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class DepartmentView(APIView):
    def post(self,request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class JobTitleView(APIView):
    def post(self,request):
        serializer=JobTitleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class EmployeeView(APIView):
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        print("TESTING 320",request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        