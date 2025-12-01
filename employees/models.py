from django.db import models


class Employee(models.Model):
    """Employee model to store employee details."""
    
    EMPLOYEE_ID = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    address = models.TextField()
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return f"{self.name} ({self.EMPLOYEE_ID})"

