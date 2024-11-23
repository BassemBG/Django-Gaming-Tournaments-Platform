from django.urls import path
from .views import Equipments_View,test_view

urlpatterns = [
    path('Equipments_View', Equipments_View, name='Equipments_View'),
    path('test/', test_view, name='test_view'),
    
]