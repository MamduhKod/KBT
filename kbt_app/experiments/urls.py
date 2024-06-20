from django.urls import path

from . import views
from .views import ExperimentTankeView

urlpatterns = [
    path("", views.Index, name="Index"),
    path("skapa/",ExperimentTankeView.as_view(), name="Skapa"),
    
    
]