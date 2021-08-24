from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('success/',views.success,name="success"),
    path('',views.login_request , name ='login'),
    path('logout/',views.logout_request , name ='logout'),
    path('register/',views.register_request , name ='register'),
    path("view_question/", views.view_question, name="view_question"),
    path("view_feed/", views.view_feed, name="view_feed"),
    path("add_question/", views.add_question, name="add_question"),
    path("question/delete/<int:id>/", views.delete_question, name="delete_question"),
    path("question/update/<int:id>/", views.update_question, name="update_question"),
    path("view_feed/add_answer/<int:id>/", views.add_answer, name="add_answer"),
    path("view_feed/view_answer/<int:id>/", views.view_answer, name="view_answer"),
]
