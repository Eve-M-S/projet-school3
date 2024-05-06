from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    id = models.IntegerField
    prenom = models.CharField( max_length=100)
    nom = models.CharField( max_length=100)
    mail = models.EmailField(max_length=100)
    adresse = models.CharField(max_length=100)
    motdepasse = models.CharField(max_length=200)

  
    # motdepasse = models.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))

# Create your models here.

     
 
