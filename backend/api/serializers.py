from rest_framework import serializers
from .models import Employee, Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    # Nested serializer to show attendance history if needed, keeping it flat for now
    class Meta:
        model = Employee
        fields = '__all__'