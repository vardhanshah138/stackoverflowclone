from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('success/',views.success,name="success"),
    path('',views.success,name="baseurl"),
    path('login/',views.login_request , name ='login'),
    path('logout/',views.logout_request , name ='logout'),
    path('register/',views.register_request , name ='register'),
]
