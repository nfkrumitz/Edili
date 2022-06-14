from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, CommandForm
from .models import Profile, Command
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CommandSerializer
# Create your views here.

def home(request):
    job = ['Peintre', 'Menuisier', 'Charpentier', 'Macon', 'Mecanicien', 'Reparateur Climatiseur', 'Plombier',
    'Electricien', 'Jardinier', 'Technicien Installateur Tele', 'Cuisinier', 'Lessiveur-Repasseur', 'Nanny',
    'Garde Enfant', 'Couturier', 'Manicure', 'Livraison', 'Demenageur', 'Coiffeur', 'Estheticien']

    context = {'job':job}
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            User = form.save()
            messages.success(request, f'Account created successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Auth/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'profile.html', context)

def commander(request, stri):
    job = stri

    form = CommandForm()
    if request.method == "POST":
        form = CommandForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            form = CommandForm()


    context = {'job': job, 'form':form}
    return render(request, 'embaucher.html', context)



class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer