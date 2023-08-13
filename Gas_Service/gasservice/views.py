from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest , RequestStatus

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer  
            service_request.save()
            return redirect('request_tracking')  
    else:
        form = ServiceRequestForm()
    
    return render(request, 'submit_service_request.html', {'form': form})

def request_tracking(request):
    customer = request.user.customer
    service_requests = ServiceRequest.objects.filter(customer=customer)
    
    return render(request, 'request_tracking.html', {'service_requests': service_requests})

def manage_requests(request):
    if request.user.is_support_representative:
        service_requests = ServiceRequest.objects.all()
        return render(request, 'manage_requests.html', {'service_requests': service_requests})
    else:
        return redirect('request_tracking')

def update_request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    if request.method == 'POST':
        form = RequestStatusForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            RequestStatus.objects.create(request=service_request, status=status)
            return redirect('manage_requests')
    else:
        form = RequestStatusForm()
    
    return render(request, 'update_request_status.html', {'form': form, 'service_request': service_request})