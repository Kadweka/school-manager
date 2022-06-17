from datetime import datetime
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render
from Management.serializer.driving_serializer.serializers import CourseSerializer, NtsaChargesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializer.general_serializer.serializers import DepartmentSerializer, EmployeeSerializer,JobTitleSerializer,UserSerializer,InstitutionSerializer
from rest_framework.response import Response
from ...models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime,requests
from rest_framework import permissions, exceptions

# Create your views here.
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
        if not request.user.is_authenticated:
            raise exceptions.PermissionDenied({
                "code":401,
                "Message":'UnAuthorized'
            })
        else:
            serializer=DepartmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data)
class JobTitleView(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            raise exceptions.PermissionDenied({
                "code":401,
                "Message":'UnAuthorized'
            })
        else:
            serializer=JobTitleSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
class EmployeeView(APIView):
    def post(self,request):
        if not request.user.is_authenticated:
            raise exceptions.PermissionDenied({
                "code":401,
                "Message":'UnAuthorized'
            })
        else:
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
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User Not Found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        else:
            payload={
                'id':user.code,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow()
            }
            token =jwt.encode(payload,'secret',algorithm='HS256')
            response=Response()
            response.set_cookie(key='jwt',value=token,httponly=True)
            response.data = ({
                "jwt":token
            })
            return response
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            # payload = jwt.decode(token,'secret',algorithms=['HS256'])
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise  AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message":"Successfully Logout"
        }
        return response

# UPDATING OUR CLASS RECORDS 