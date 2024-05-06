from django import forms
from django.db import models

from django.contrib.auth.models import User


class modif(forms.Form):
    prenom = forms.CharField(label="prenom", max_length=100)
    nom = forms.CharField(label="nom", max_length=100)
    mail = forms.EmailField(label="mail", max_length=100)
    adresse = forms.CharField(label="adresse", max_length=100)
    motdepasse = forms.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))



    

    
