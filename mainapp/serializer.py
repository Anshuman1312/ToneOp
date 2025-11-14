from rest_framework import serializers
from .models import *

class School_serializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        
class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"