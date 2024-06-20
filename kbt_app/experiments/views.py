from django.shortcuts import render
from django.views.generic import CreateView
from .models import Experiment, ExperimentPlan
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
class ExperimentTankeView(CreateView):
    model = ExperimentPlan
    fields = ["negativ_tanke","Hypotes", "tro_pre"]
    success_url = reverse_lazy(('Experiment'))
    
    def render_to_response(self, context, **kwargs):
        context['form'] = self.get_form()
        return super().render_to_response(context, **kwargs)
    

#def Index(request):
 #   experiment= ExperimentPlan.objects.all()
  ## return render(request,'experiments/index.html', context)



    

    
    
    
    