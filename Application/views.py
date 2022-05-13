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
    return render(request, 'home.html')

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

def commander(request):

    return render(request, 'embaucher.html', {'form':form})


def macon(request):

    """fonction billing():
        qui retourne 0 si l'employeur a de l'argent sur son compte et 1 si il en a pas
    """

    form = CommandForm(request.POST or None)
    worker = Command()    
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'macon'
        tmac = User.profile.get_queryset()
        post.target = []
        for i in tmac:
            if i.job == 'Macon':
                post.target.append(i)
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/macon.html', {'form':form})

def plomblier(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'plomblier'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/plombier.html', {'form':form})

def repclim(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'reparateur climatiseur'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/repclim.html', {'form':form})

def coiffeur(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'coiffeur'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/coiffeur.html', {'form':form})

def electricien(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'electricien'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/electricien.html', {'form':form})

def jardinier(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'jardinier'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/jardinier.html', {'form':form})

def cuisinier(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'cuisinier'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/cuisinier.html', {'form':form})

def mecanicien(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'mecanicien'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/mecanicien.html', {'form':form})

def lessiveur(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'lessiveur'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/lessiveur.html', {'form':form})

def gardenf(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'garde enfants'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/gardenf.html', {'form':form})

def couturier(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'couturier'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/couturier.html', {'form':form})

def makeup(request):
    form = CommandForm(request.POST or None)
        
    if form.is_valid():
        post = form.save(commit=False)
        post.ouvrier = 'makeup'
        form.save()

    else:
        form = CommandForm()
    return render(request, 'job/makeup.html', {'form':form})


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer