from django.shortcuts import render
from django.views import generic
from .models import Experiment
from django.http import HttpResponse

# Create your views here.
def Index(request):
    experiment= Experiment.objects.all()
    context = {'experiments': experiment}
    return render(request,'experiments/index.html', context)
    
    
    