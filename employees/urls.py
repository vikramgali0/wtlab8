from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<str:employee_id>/', views.employee_detail, name='employee_detail'),
]

