from pyexpat import model
from rest_framework import serializers
from ..models import User,InstitutionData

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionData
        fields=['name','email','tel','institution_tin','institution_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','instituon_code','email']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
