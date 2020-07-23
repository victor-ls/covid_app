from django.urls import path
from .views import list_patients, create_patient, update_patient, delete_patient

urlpatterns = [
    path('', list_patients, name='list_patients'),
    path('create', create_patient, name='create_patients'),
    path('update/<int:id>', update_patient, name='update_patient'),
    path('delete/<int:id>', delete_patient, name='delete_patient')
]