from datetime import datetime
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializer.driving_serializer.serializers import CourseSerializer
from rest_framework.response import Response
from ...models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime,requests
from rest_framework import permissions, exceptions



class CourseView(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            raise exceptions.PermissionDenied({
                "code":401,
                "Message":'UnAuthorized'
            })
        else:
            serializer=CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)