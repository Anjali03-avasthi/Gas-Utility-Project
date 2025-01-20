from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('', views.homepage, name='homepage'),  
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
    path('logout/', views.logout_view, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
