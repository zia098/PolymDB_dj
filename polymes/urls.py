from django.urls import path
from .views import polymerase_list



urlpatterns = [
    path('', polymerase_list, name='polymerase_list'),
]
