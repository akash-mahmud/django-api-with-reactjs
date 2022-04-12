from django.db.models.base import Model
from rest_framework import serializers

from EmployeeApp.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields= ('departmentId',
        'departmentName'
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        Model= Employee
        fields= ('employeeId',
        'employeeName',
        'department',
        'dateOfJoining',
        'photoFileName',
        )