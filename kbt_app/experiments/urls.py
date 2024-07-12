from django.urls import path

from . import views
from .views import ExperimentPlanView, DeleteExperiment

urlpatterns = [
    path("", views.Index, name="Index"),
    path('<int:experiment_id>/',views.Detail, name='Detail'),
    path("skapa/",ExperimentPlanView.as_view(), name="Skapa"), 
    path('<int:experiment_id>/registrera',views.Registrera, name='Registrera'),
    path('<int:experiment_id>/registrera/resultat/<int:resultat_id>',views.Resultat, name='Resultat'), 
    path('<int:pk>/delete/', DeleteExperiment.as_view(), name='delete'), 
]