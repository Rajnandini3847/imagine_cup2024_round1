from .views import *
from django.urls import path,include

urlpatterns = [
    path('', landing_page, name='landing_page'),
]