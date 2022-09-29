from django.urls import path
from . import views

urlpatterns = [
    path('', views.hrms, name = 'hrms'),

]