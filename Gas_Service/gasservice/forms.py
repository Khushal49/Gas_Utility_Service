from django import forms
from .models import ServiceRequest, RequestStatus

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']
        

class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = RequestStatus
        fields = ['status']

