from django.urls import path

from . import views
from .views import ExperimentCreateView

urlpatterns = [
    path("", views.Index, name="Index"),
    path("<int:experiment_id>", views.Detail, name="Detail"),
    path("skapa/",ExperimentCreateView.as_view(), name="Skapa"),
    
    
]