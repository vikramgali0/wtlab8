from django.shortcuts import render, get_object_or_404
from .models import Employee


def employee_list(request):
    """Display list of all employees."""
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'total_employees': employees.count()
    }
    return render(request, 'employees/employee_list.html', context)


def employee_detail(request, employee_id):
    """Display detailed information about a specific employee."""
    employee = get_object_or_404(Employee, EMPLOYEE_ID=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'employees/employee_detail.html', context)

