from django.urls import path
from .views import polymerase_list
from . import views
from .views import polymerase_list, wildtype_detail, modified_detail, domain_detail



urlpatterns = [
    path('', polymerase_list, name='polymerase_list'),

    path('wildtype/<int:pk>/', wildtype_detail, name='wildtype_detail'),
    path('modified/<int:pk>/', modified_detail, name='modified_detail'),
    path('domain/<int:pk>/', domain_detail, name='domain_detail'),
]
