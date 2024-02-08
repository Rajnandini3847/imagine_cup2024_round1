from .views import *
from django.urls import path,include

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('restaurants/', restaurants, name='restaurants'),
    path('hospitals/', hospitals, name='hospitals'),
    path('schools_and_colleges/', schools_and_colleges, name='schools_and_colleges'),
    path('jobs/', job_list, name='job_list'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path('jobs/<int:job_id>/apply/', apply_for_job, name='apply_for_job'),
    
]