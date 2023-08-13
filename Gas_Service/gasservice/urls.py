# consumer_services/urls.py
from django.urls import path
from . import views

app_name = 'gasservices'

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/', views.request_tracking, name='request_tracking'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('update/<int:request_id>/', views.update_request_status, name='update_request_status'),
]
