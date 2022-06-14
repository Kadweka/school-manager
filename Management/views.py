from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer.serializers import UserSerializer,InstitutionSerializer
from rest_framework.response import Response
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

class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        