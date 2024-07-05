from django import forms
from .models import ExperimentResultat, ExperimentPlan

class RegistreraResultat(forms.ModelForm):
    Experiment = forms.ModelChoiceField(queryset=ExperimentPlan.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = ExperimentResultat
        fields = ('Experiment','resultat', 'insikter', 'tro_post')