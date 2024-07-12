from django import forms
from .models import ExperimentResultat, ExperimentPlan

class RegistreraResultat(forms.ModelForm):
    Experiment = forms.ModelChoiceField(queryset=ExperimentPlan.objects.all(), widget=forms.HiddenInput())
    tro_pre_stored = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = ExperimentResultat
        fields = ('Experiment','resultat', 'insikter', 'tro_post', 'tro_pre_stored')