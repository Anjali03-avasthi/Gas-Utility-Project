import os
from django.db import connection
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import ServiceRequest
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'service_requests/register.html', {'error': 'Passwords do not match'})

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

       
        next_url = request.POST.get('next', 'register')
        return redirect(next_url)  

    return render(request, 'service_requests/register.html')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  
    
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage') 
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def homepage(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    user_service_requests = ServiceRequest.objects.filter(customer__user=request.user)
    
    return render(request, 'home.html', {'user_service_requests': user_service_requests})


def submit_request(request):
    if not request.user.is_authenticated:
        return redirect(f'{reverse("register")}?next={request.path}')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        service_type = request.POST['service_type']
        request_details = request.POST['request_details']
        attachment = request.FILES.get('attachment', None)

        file_path = None
        if attachment:
            file_name = default_storage.save(os.path.join('uploads', attachment.name), ContentFile(attachment.read()))
            file_path = default_storage.url(file_name)

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO service_requests 
                (first_name, last_name, email, phone, service_type, request_details, attachment) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [first_name, last_name, email, phone, service_type, request_details, file_path])

        return redirect('track_requests')

    return render(request, 'service_requests/submit_request.html')

def track_requests(request):
    if not request.user.is_authenticated:
        return redirect(f'{reverse("register")}?next={request.path}') 
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, 
                   first_name || ' ' || last_name AS customer_name, 
                   service_type, 
                   request_details, 
                   created_at,
                    status, 
                   resolved_at, 
                   attachment
            FROM service_requests 
            ORDER BY created_at DESC
        """)
        rows = cursor.fetchall()
    
    indexed_rows = [(index + 1, *row) for index, row in enumerate(rows)]

    return render(request, 'service_requests/track_requests.html', {'requests': indexed_rows})

def update_request_status(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    
    if request.method == "POST":
        status = request.POST.get('status')
        if status == 'Resolved':
            service_request.status = 'Resolved'
            service_request.resolved_at = timezone.now()
        else:
            service_request.status = status
        service_request.save()
    
    return redirect('track_requests')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages







