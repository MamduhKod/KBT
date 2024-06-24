from .models import ExperimentPlan, ExperimentResultat
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def Index(request):
    experiments = ExperimentPlan.objects.all() 
    context = {'experiments': experiments}  
    return render(request, 'experiments/index.html', context)

def Detail(request,experiment_id):
    experiment = get_object_or_404(ExperimentPlan, pk=experiment_id)
    context = {'detail': experiment}
    return render(request, 'experiments/experiment_detail.html',context)
    

class ExperimentPlanView(CreateView):
    model = ExperimentPlan
    fields = ["negativ_tanke","tro_pre","datum","Beteende","Situation","Konsekvens"]
    success_url = reverse_lazy('Index')
    
    def get(self, request, *args, **kwargs):
     context = {} 
     context['form'] = self.get_form()
     return render(request, 'experiments/tanke_form.html', context)


class ExperimentResultatView(CreateView):
    model = ExperimentResultat
    fields = ["resultat","insikter","tro_post"]
    success_url = reverse_lazy(('Resultat'))
    
    def get(self, request, *args, **kwargs):
     context = {} 
     context['form'] = self.get_form()
     return render(request, 'experiments/record_result.html', context)
    
    
def Resultat(request,experiment_id ):
    resultat = ExperimentResultat.objects.get(pk=experiment_id)  
    context = {'resultat': resultat}  
    return render(request, 'experiments/result.html', context)
