from django.db import models
from django.utils import timezone 
from datetime import date
# Create your models here.

from django.apps import AppConfig

class ExperimentsConfig(AppConfig):
    name = 'experiments' 
    
    
class ExperimentPlan(models.Model):
    negativ_tanke = models.CharField( max_length=50,
        help_text="Vilken tanke vill du testa?")
    tro_pre = models.IntegerField(help_text="Hur starkt tror du på din förutsägelse?")
    datum = models.DateField(default=date.today)
    Beteende = models.CharField( max_length=100,
        help_text="Hur kan du testa din tanke?")
    Situation = models.CharField( max_length=100,
        help_text="Var kan du testa din tanke?")
    Konsekvens = models.CharField(max_length=100,
        help_text="Vad tror du kommer hända?")
    

    
class ExperimentResultat(models.Model):
    Experiment = models.ForeignKey(ExperimentPlan, on_delete=models.CASCADE)
    resultat = models.CharField(max_length=300,help_text="Vad hände?")
    insikter = models.CharField( max_length=300, help_text="Vilka insikter kom du till?")
    tro_post = models.SmallIntegerField(help_text="Hur starkt tror du på din ursprungliga tanke nu?")
    tro_pre_stored = models.SmallIntegerField(blank=True, null=True)
    tro_post_skillnad = models.SmallIntegerField(blank=True, null=True)
    
    @property
    def tro_post_skillnad(self):
       if self.tro_post and self.tro_pre_stored:
           return self.tro_post - self.tro_pre_stored
       else:
           return None
       
    def __str__(self):
        return self.results_text
    