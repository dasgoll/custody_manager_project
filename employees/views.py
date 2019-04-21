from django.shortcuts import render
from .models import Employee


def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/employees.html', context)
