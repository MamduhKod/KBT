from .models import ExperimentPlan, ExperimentResultat
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.


def Index(request):
    experiments = ExperimentPlan.objects.all()  
    context = {'experiments': experiments}  
    return render(request, 'experiments/index.html', context)

class ExperimentPlanView(CreateView):
    model = ExperimentPlan
    fields = ["negativ_tanke","namn", "beskrivning","Beteende","Situation","Konsekvens","datum","tro_pre"]
    success_url = reverse_lazy(('Index'))
    
    def get(self, request, *args, **kwargs):
     context = {} 
     context['form'] = self.get_form()
     return render(request, 'experiments/tanke_form.html', context)


    

    
    
    
    