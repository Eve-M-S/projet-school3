from django import forms 


class create_product(forms.Form):
    identifier= forms.CharField(label="identifier", max_length=100)
    prix = forms.CharField(label="prix", max_length=100)
    description = forms.CharField(label="description", max_length=100)
    stock= forms.CharField(label="stock", max_length=100)

class remove_product(forms.Form):
    identifier= forms.CharField(label="identifier", max_length=100)

class Update_product(forms.Form):
   
    identifier= forms.CharField(label="identifier", max_length=100)
    prix = forms.CharField(label="prix", max_length=100)
    description = forms.CharField(label="description", max_length=100)
    stock= forms.CharField(label="stock", max_length=100)
    

class create_User(forms.Form):
    nom = forms.CharField(label="nom", max_length=100)
    prenom = forms.CharField(label="prenom", max_length=100)
    mail = forms.EmailField(label="mail", max_length=100)
    adresse = forms.CharField(label="adresse", max_length=100)
    statut = forms.CharField(label="statut", max_length=100)
    motdepasse = forms.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))

class update_User(forms.Form):
  
    nom = forms.CharField(label="nom", max_length=100)
    prenom = forms.CharField(label="prenom", max_length=100)
    mail = forms.EmailField(label="mail", max_length=100)
    adresse = forms.CharField(label="adresse", max_length=100)
    statut = forms.CharField(label="statut", max_length=100)
    motdepasse = forms.CharField(label="mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'password-input'}))



class remove_user(forms.Form):
    mail = forms.EmailField(label="mail", max_length=100)



   