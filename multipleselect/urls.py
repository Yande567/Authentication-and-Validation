from django.urls import path
from . import views

urlpatterns = [
    path('application_form/<str:job_title>/', views.ApplicationForm.as_view(), name='application_form'),
]
