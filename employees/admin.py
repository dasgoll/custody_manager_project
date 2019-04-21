from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'hire_date')
    list_display_links = ('id', 'name')


admin.site.register(Employee, EmployeeAdmin)
