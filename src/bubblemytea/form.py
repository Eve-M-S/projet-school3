from django import forms 


class myForm(forms.Form):
    nom = forms.CharField(label="nom", max_length=100)
    prenom = forms.CharField(label="prenom", max_length=100)
    mail = forms.EmailField(label="mail", max_length=100)
    adresse = forms.CharField(label="adresse", max_length=100)
    motdepasse = forms.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))

class login(forms.Form):
    mail = forms.EmailField(label="mail", max_length=100)
    motdepasse = forms.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))



   