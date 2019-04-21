from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('<int:emp_id>', include('custodies.urls')),
]