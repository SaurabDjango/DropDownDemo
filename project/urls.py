from django.urls import path,include
from project import views

urlpatterns = [
    
    path('table', views.table, name='table'),
]
