from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EMPLOYEE_ID', 'name', 'email', 'department', 'position', 'hire_date')
    list_filter = ('department', 'position', 'hire_date')
    search_fields = ('EMPLOYEE_ID', 'name', 'email', 'department')
    ordering = ('name',)

