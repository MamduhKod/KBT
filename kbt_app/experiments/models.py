from django.db import models

# Create your models here.

from django.apps import AppConfig

class ExperimentsConfig(AppConfig):
    name = 'experiments' 
    
    
class Experiment(models.Model):
    namn = models.CharField(max_length=50,)
    beskrivning = models.CharField(help_text="Beskriv syftet med ditt experiment.", max_length=300)
    datum = models.DateField(auto_now=False, auto_now_add=False, 
    help_text="När vill du utföra ditt experiment?")
    def __str__(self):
        return self.experiment_text
    
class Kognition(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    negativ_tanke = models.CharField( max_length=50)
    antagande = models.CharField( max_length=300)
    
    def __str__(self):
        return self.kognition_text

class ExperimentPlan(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    Beteende = models.CharField( max_length=100)
    Situation = models.DateField( max_length=100)
    Konsekvens = models.DateField(max_length=100)
    
    def __str__(self):
        return self.experiment_plan_text
class Hypotes(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    hypotes = models.CharField(max_length=300)
    tro_pre = models.SmallIntegerField()
    
    def __str__(self):
        return self.hypotes_text

class Resultat(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    resultat = models.CharField(max_length=300)
    tro_post = models.SmallIntegerField()
    
    def __str__(self):
        return self.results_text

class Insikt(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    insikter = models.CharField( max_length=300)
    tro_skillnad = models.SmallIntegerField()
    
    def __str__(self):
        return self.insikt_text
    
