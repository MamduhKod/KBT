from .models import ExperimentPlan, ExperimentResultat
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import ExperimentResultForm

# Create your views here.


def Index(request):
    experiments = ExperimentPlan.objects.all()  
    context = {'experiments': experiments}  
    
    if request.method == "POST":
     experiment_id = request.POST.get('experiment_id')
     experiment = ExperimentPlan.objects.get(pk=experiment_id)
     form = ExperimentResultForm(request.POST)
     
     if form.is_valid():
         result = form.save(commit=False)  
         result.Experiment = experiment  
         result.tro_pre_stored = experiment.tro_pre 
         result.save()  
         return redirect('index')
    
    
    return render(request, 'experiments/index.html', context)

class ExperimentPlanView(CreateView):
    model = ExperimentPlan
    fields = ["negativ_tanke","tro_pre","datum","Beteende","Situation","Konsekvens"]
    success_url = reverse_lazy(('Index'))
    
    def get(self, request, *args, **kwargs):
     context = {} 
     context['form'] = self.get_form()
     return render(request, 'experiments/tanke_form.html', context)


def record_result(request, experiment_id):
    if request.method == 'POST':
        form = ExperimentResultForm(request.POST)
        if form.is_valid():
            # Save the form data (process results)
            # ... (your logic to save results)
            return redirect('experiments:index')  # Redirect to experiments list after saving
    else:
        form = ExperimentResultForm()
    context = {'form': form, 'experiment_id': experiment_id}
    return render(request, 'experiments/record_result.html', context)

    
    
    
    