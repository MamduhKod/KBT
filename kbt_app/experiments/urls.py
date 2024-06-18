from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index, name="Index"),
    path("Detail/", views.Detail, name="Detail"),
    
    
]