from django.shortcuts import render
from django.views import generic
from .models import Experiment
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    return HttpResponse('Hi')
    
    
    