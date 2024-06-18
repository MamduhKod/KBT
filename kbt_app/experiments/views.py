from django.shortcuts import render
from django.views.generic import CreateView
from .models import Experiment, ExperimentPlan
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
def Index(request):
    experiment= Experiment.objects.all()
    context = {'experiments': experiment}
    return render(request,'experiments/index.html', context)

def Detail(request):
    experiment_detail = ExperimentPlan.objects.all()
    context = {'experiment_detail': experiment_detail}
    return render(request,'experiments/index.html', context)


 class EgenForm(models.Model):
            class Meta:
            model = Experiment
   class ExperimentCreateView(CreateView):
    model = Experiment
    fields = ["namn","beskrivning", "datum"]
    success_url = reverse_lazy(('Index'))
    

    
    
    
    