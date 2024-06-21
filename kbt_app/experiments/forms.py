from django import forms
from .models import ExperimentResultat

class ExperimentResultForm(forms.ModelForm):
    class Meta:
        model = ExperimentResultat
        fields = ('resultat', 'insikter', 'tro_post')