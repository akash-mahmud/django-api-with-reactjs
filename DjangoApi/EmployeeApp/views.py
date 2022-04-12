from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage
@csrf_exempt
def departmentApi(request, id=0):
    if request.method== 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe= False)
    elif request.method== 'POST':
         department_data = JSONParser().parse(request)
         print(department_data)

         departments_serializer= DepartmentSerializer(data=department_data)
         if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse("Added Succesfull !!" , safe=False)
         print(request)
         return JsonResponse("Added failed !!" , safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(departmentId=department_data['departmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
             departments_serializer.save()
             return JsonResponse("Updated Succesfull !!" , safe=False)
        return JsonResponse("Added failed !!" , safe=False)
    elif request.method == 'DELETE':
       
        department = Department.objects.get(departmentId= id)
        department.delete()
        
        return JsonResponse("deleted successful !!" , safe=False)



@csrf_exempt
def employeeApi(request, id=0):
    if request.method== 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe= False)
    elif request.method== 'POST':
         employee_data = JSONParser().parse(request)
         print(employee_data)

         employees_serializer= DepartmentSerializer(data=employee_data)
         if employees_serializer.is_valid():
             employees_serializer.save()
             return JsonResponse("Added Succesfull !!" , safe=False)
         print(request)
         return JsonResponse("Added failed !!" , safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employees = Employee.objects.get(employeeId=employee_data['employeeId'])
        employees_serializer = DepartmentSerializer(employees, data=employee_data)
        if employees_serializer.is_valid():
             employees_serializer.save()
             return JsonResponse("Updated Succesfull !!" , safe=False)
        return JsonResponse("Added failed !!" , safe=False)
    elif request.method == 'DELETE':
       
        employees = Employee.objects.get(employeeId= id)
        employees.delete()
        
        return JsonResponse("deleted successful !!" , safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name , file)

    return JsonResponse(file_name , safe=False)
# Create your views here.

