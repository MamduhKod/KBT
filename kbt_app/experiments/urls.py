from django.urls import path

from . import views
from .views import ExperimentPlanView

urlpatterns = [
    path("", views.Index, name="Index"),
    path("skapa/",ExperimentPlanView.as_view(), name="Skapa"), 
    path('experiments/<int:experiment_id>/record_result/', views.record_result, name='record_result'),   
    
    
]