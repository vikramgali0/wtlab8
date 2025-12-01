from django.core.management.base import BaseCommand
from employees.models import Employee
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Loads sample employee data into the database'

    def handle(self, *args, **options):
        # Sample employee data
        employees_data = [
            {
                'EMPLOYEE_ID': 'EMP001',
                'name': 'John Smith',
                'email': 'john.smith@company.com',
                'phone': '+1-555-0101',
                'department': 'Engineering',
                'position': 'Senior Software Engineer',
                'salary': 95000.00,
                'hire_date': date(2020, 3, 15),
                'address': '123 Tech Street, San Francisco, CA 94102, USA'
            },
            {
                'EMPLOYEE_ID': 'EMP002',
                'name': 'Sarah Johnson',
                'email': 'sarah.johnson@company.com',
                'phone': '+1-555-0102',
                'department': 'Marketing',
                'position': 'Marketing Manager',
                'salary': 85000.00,
                'hire_date': date(2019, 7, 22),
                'address': '456 Market Avenue, New York, NY 10001, USA'
            },
            {
                'EMPLOYEE_ID': 'EMP003',
                'name': 'Michael Chen',
                'email': 'michael.chen@company.com',
                'phone': '+1-555-0103',
                'department': 'Sales',
                'position': 'Sales Representative',
                'salary': 65000.00,
                'hire_date': date(2021, 1, 10),
                'address': '789 Sales Boulevard, Los Angeles, CA 90001, USA'
            },
            {
                'EMPLOYEE_ID': 'EMP004',
                'name': 'Emily Davis',
                'email': 'emily.davis@company.com',
                'phone': '+1-555-0104',
                'department': 'Human Resources',
                'position': 'HR Specialist',
                'salary': 70000.00,
                'hire_date': date(2020, 9, 5),
                'address': '321 HR Plaza, Chicago, IL 60601, USA'
            },
            {
                'EMPLOYEE_ID': 'EMP005',
                'name': 'David Wilson',
                'email': 'david.wilson@company.com',
                'phone': '+1-555-0105',
                'department': 'Finance',
                'position': 'Financial Analyst',
                'salary': 75000.00,
                'hire_date': date(2021, 5, 18),
                'address': '654 Finance Road, Boston, MA 02101, USA'
            }
        ]

        # Clear existing employees (optional - comment out if you want to keep existing data)
        Employee.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing employees...'))

        # Create employees
        created_count = 0
        for emp_data in employees_data:
            employee, created = Employee.objects.get_or_create(
                EMPLOYEE_ID=emp_data['EMPLOYEE_ID'],
                defaults=emp_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created employee: {employee.name} ({employee.EMPLOYEE_ID})')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Employee already exists: {employee.name} ({employee.EMPLOYEE_ID})')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully loaded {created_count} employees!')
        )

