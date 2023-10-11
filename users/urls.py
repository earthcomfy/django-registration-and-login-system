
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='users-home'),
    # path('home/', views.home_view, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('add_client/', views.add_client, name='add_client'),
    path('success/', views.success_view, name='success_page'),
    path('success/', views.attendance_success, name='attendance_success'),  
    
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('attendance/', views.record_attendance, name='record_attendance'),
    
    path('user-clients/', views.user_clients, name='user_clients'),
    # path('admin-clients/', views.admin_clients, name='admin_clients'),
    path('client/<int:pk>/', views.client_details, name='client_details'),

  
]
