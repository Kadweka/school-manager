from pyexpat import model
from rest_framework import serializers
from ...system_module.general_models.models import InstitutionEmployee,InstitutionData,InstitutionDepartment,InstitutionJobTitle
from ...models import User

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionData
        fields=['name','email','tel','institution_tin','institution_type']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionDepartment
        fields=['name','institution_code']
       

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionJobTitle
        fields=['name','department_code']
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionEmployee
        fields=['national_id','is_user','kra_pin','mobile','institution_code','email','first_name','last_name','job_title_code']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','password','institution_code','email']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
    
