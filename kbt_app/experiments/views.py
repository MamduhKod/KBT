from .models import ExperimentPlan, ExperimentResultat
from experiments.forms import RegistreraResultat
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

def Registrera(request, experiment_id):
    experiment_plan = get_object_or_404(ExperimentPlan,pk=experiment_id)
    if request.method == "POST":
        form = RegistreraResultat(request.POST)
    if form.is_valid():
        
        form.save()
        return redirect('Index')
    else:
        form = RegistreraResultat(initial={"experiment": experiment_plan})
    context = {"form": form, "experiment":experiment_plan}
    return render(request,"experiments/record_results.html", context)

        
        
    