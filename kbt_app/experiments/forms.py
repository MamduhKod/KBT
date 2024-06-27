from django import forms
from .models import ExperimentResultat

#not used rn.

class RegistreraResultat(forms.ModelForm):
    class Meta:
        model = ExperimentResultat
        fields = ('resultat', 'insikter', 'tro_post')