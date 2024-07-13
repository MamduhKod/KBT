from .models import ExperimentPlan, ExperimentResultat
from experiments.forms import RegistreraResultat
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from .forms import SignupForm
from django.contrib.auth import get_user_model, UserCreationForm



# Create your views here.

def Index(request):
    experiments = ExperimentPlan.objects.all() 
    resultat = ExperimentResultat.objects.all()
    context = {'experiments': experiments, 'resultat':  resultat}  
    return render(request, 'experiments/index.html', context)

def Detail(request,experiment_id):
    experiment = get_object_or_404(ExperimentPlan, pk=experiment_id)
    context = {'detail': experiment}
    return render(request, 'experiments/experiment_detail.html',context)
    

class ExperimentPlanView(CreateView):
    model = ExperimentPlan
    fields = ["negativ_tanke","tro_pre","datum","Beteende","Situation","Konsekvens"]
    success_url = reverse_lazy('Index')
    
    def get(self, request, *args, **kwargs):
     context = {} 
     context['form'] = self.get_form()
     return render(request, 'experiments/record_plan.html', context)

def Registrera(request, experiment_id):
    experiment_plan = get_object_or_404(ExperimentPlan,pk=experiment_id) 
    tro_pre = experiment_plan.tro_pre
    existing_result = ExperimentResultat.objects.filter(Experiment=experiment_plan).exists()

    if existing_result:
        # Result already exists, hide the form (optional message)
        context = {"message": "Ett resultat har redan registrerats för detta experiment."}
        return render(request, "experiments/record_result.html", context)
    else:
     form = RegistreraResultat(initial={"Experiment": experiment_plan,"tro_pre_stored":tro_pre})
    if request.method == "POST":
        form = RegistreraResultat(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Resultat', experiment_id=experiment_id, resultat_id=form.instance.pk)
    
    context = {"formR": form, "experiment":experiment_plan}
    return render(request,"experiments/record_result.html", context)

def Resultat(request, experiment_id, resultat_id):
    experiment_resultat = get_object_or_404(ExperimentResultat, pk=resultat_id)
    experiment_plan = get_object_or_404(ExperimentPlan, pk=experiment_id)
    tro_pre = experiment_plan.tro_pre
    tro_post = experiment_resultat.tro_post
    tro_skillnad = tro_pre - tro_post

    context = {
        'experiment_plan':experiment_plan,
        'experiment_id': experiment_id,
        'tro_skillnad': tro_skillnad,
        'belief_message': '', 
    }

    if tro_skillnad > 0:
        context['belief_message'] = 'Din initiala tro verkar ha minskat något efter experimentet. Du tror mindre på din tanke.'  # Belief went down
    elif tro_skillnad < 0:
        context['belief_message'] = 'Din initiala tro verkar ha ökat något efter experimentet. Du tror mer på din tanke.'  # Belief went up
    else:
        context['belief_message'] = 'Din initiala tro verkar vara densamma efter experimentet. Du tror varken mer eller mindre på din tanke.'  # Belief stayed the same

    return render(request, 'experiments/result.html', context)

class DeleteExperiment(DeleteView):
    model = ExperimentPlan  # Replace with your experiment model

    success_message = "Du har raderat din experimentplan, och eventuella resultat kopplade till planen."
    template_name = "experiments/delete_confirmation.html"  # Customize template

    def get_success_url(self):
        return reverse("Index")  # Redirect to index after deletion

    # Optional: Add logic to restrict deletion based on conditions (e.g., user permissions)


def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()  # Saves the new user to the database
      # Redirect to a success page or login page
      return redirect('login')  # Replace with your desired redirect URL
  else:
    form = SignupForm()
  return render(request, 'signup.html', {'form': form})
    