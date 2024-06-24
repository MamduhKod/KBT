from django.urls import path

from . import views
from .views import ExperimentPlanView, ExperimentResultatView

urlpatterns = [
    path("", views.Index, name="Index"),
    path('<int:experiment_id>/',views.Detail, name='Detail'),
    path("skapa/",ExperimentPlanView.as_view(), name="Skapa"), 
    path('<int:experiment_id>/record_result/', ExperimentResultatView.as_view(), name='Klart_experiment'),
    path('<int:experiment_id>/record_result/result', views.Resultat, name='Resultat'),    
    
]