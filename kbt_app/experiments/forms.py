from django import forms
from .models import ExperimentResultat, ExperimentPlan
from django.contrib.auth import get_user_model, UserCreationForm

class RegistreraResultat(forms.ModelForm):
    Experiment = forms.ModelChoiceField(queryset=ExperimentPlan.objects.all(), widget=forms.HiddenInput())
    tro_pre_stored = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = ExperimentResultat
        fields = ('Experiment','resultat', 'insikter', 'tro_post', 'tro_pre_stored')
        

User = get_user_model()

class SignupForm(forms.UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']