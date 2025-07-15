from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list_view, name='employee-list'),
]
