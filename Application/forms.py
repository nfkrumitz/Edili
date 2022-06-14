from django import forms
from django.contrib.auth.models import User
from .models import Profile, Command

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['job', 'zone', 'image']


"""class CommandForm(forms.ModelForm):
	class Meta:
		model = Command
		fields = ['nom', 'prenom', 'zone', 'telephone', 'ouvrier']"""

class CommandForm(forms.ModelForm):
	class Meta:
		model = Command
		fields = ['nom', 'prenom', 'telephone', 'zone']