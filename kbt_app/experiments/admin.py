from django.contrib import admin

from .models import ExperimentPlan, ExperimentResultat

# Register your models here.

admin.site.register(ExperimentPlan)
admin.site.register(ExperimentResultat)
