from django.db import models

# Create your models here.

from django.apps import AppConfig

class ExperimentsConfig(AppConfig):
    name = 'experiments' 
    
    
class ExperimentPlan(models.Model):
    namn = models.CharField(max_length=50,)
    Hypotes = models.CharField(max_length=100, 
     help_text="Vad tror du kommer hända?")
    negativ_tanke = models.CharField( max_length=50,
        help_text="Vilken tanke vill du testa?")
    beskrivning = models.CharField(help_text="Beskriv syftet med ditt experiment.", max_length=300)
    datum = models.DateField(auto_now=False, auto_now_add=False, 
    help_text="När vill du utföra ditt experiment?")
    Beteende = models.CharField( max_length=100)
    Situation = models.DateField( max_length=100)
    Konsekvens = models.DateField(max_length=100)
    tro_pre = models.SmallIntegerField(help_text="Hur starkt tror du på din förutsägelse?")

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
    