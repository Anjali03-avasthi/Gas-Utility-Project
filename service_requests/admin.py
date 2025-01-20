from django.contrib import admin
from .models import Customer, ServiceRequest, RequestStatusUpdate, User 

admin.site.register(Customer)
admin.site.register(ServiceRequest)
admin.site.register(RequestStatusUpdate)
admin.site.register(User)
