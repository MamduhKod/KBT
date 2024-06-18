from django.db import models

# Create your models here.
class Experiment(models.Model):
    namn = models.CharField( max_length=50)
    beskrivning = models.CharField( max_length=300)
    datum = models.DateField(auto_now=False, auto_now_add=False)
    
class Kognition(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    negativ_tanke = models.CharField( max_length=50)
    antagande = models.CharField( max_length=300)

class ExperimentPlan(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    Beteende = models.CharField( max_length=100)
    Situation = models.DateField( max_length=100)
    Konsekvens = models.DateField(max_length=100)
    
class Hypotes(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    hypotes = models.CharField(max_length=300)
    tro_pre = models.SmallIntegerField()

class Resultat(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    resultat = models.CharField(max_length=300)
    tro_post = models.SmallIntegerField()

class Insikt(models.Model):
    Experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    insikter = models.CharField( max_length=300)
    tro_skillnad = models.SmallIntegerField()