from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)

class RequestStatus(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)