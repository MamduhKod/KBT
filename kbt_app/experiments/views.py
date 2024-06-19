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
    return render(request,'experiments/detail.html', context)


class ExperimentCreateView(CreateView):
    model = Experiment
    fields = ["namn","beskrivning", "datum"]
    success_url = reverse_lazy(('Index'))
    
    def render_to_response(self, context, **kwargs):
        context['form'] = self.get_form()
        return super().render_to_response(context, **kwargs)
    
    

    
    
    
    