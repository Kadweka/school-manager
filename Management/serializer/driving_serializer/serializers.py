from pyexpat import model
from rest_framework import serializers
from ...system_module.driving_models.models import CourseData, NtsaCharges


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseData
        fields=['name','description','total_payable','institution_code']

class NtsaChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model=NtsaCharges
        fields=['name','amount','institution_code']
       