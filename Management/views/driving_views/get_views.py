from datetime import datetime
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render
from Management.system_module.driving_models.models import CourseData, NtsaCharges
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializer.driving_serializer.serializers import CourseSerializer, NtsaChargesSerializer
from rest_framework.response import Response
from ...models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime,requests
from rest_framework import permissions, exceptions



class GetCourseView(APIView):
    def get(self,request):
        course=CourseData.objects.all()
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)
class GetNtsaView(APIView):
    def get(self,request):
        course=NtsaCharges.objects.all()
        serializer=NtsaChargesSerializer(course,many=True)
        return Response(serializer.data)



        