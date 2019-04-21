from django.shortcuts import render
from .models import Custody
from employees.models import Employee


def custodies(request, emp_id):
    custodies = Custody.objects.filter(employee=emp_id)
    emps = Employee.objects.filter(id=emp_id)
    context = {'custodies': custodies, 'emps': emps}
    return render(request, 'custodies/custodies.html', context)
