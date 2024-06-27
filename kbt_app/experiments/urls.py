from django.urls import path

from . import views
from .views import ExperimentPlanView

urlpatterns = [
    path("", views.Index, name="Index"),
    path('<int:experiment_id>/',views.Detail, name='Detail'),
    path("skapa/",ExperimentPlanView.as_view(), name="Skapa"), 
    path('<int:experiment_id>/registrera',views.Registrera, name='Registrera'),    
]