from django.urls import path
from .views import *

urlpatterns = [
    path('cars/',CarsList.as_view(),name ='cars_list'),
   
]
