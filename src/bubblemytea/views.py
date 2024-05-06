from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken
import jwt


from .form import myForm,login
from user.models import User
date =datetime.today()
# Create your views here.


def get_form(request):
    if request.method == "GET":
        return render(request,"bubblemytea/index.html", context={"form":myForm,"date":date})
 
    if request.method == "POST":
        form = myForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            mail = form.cleaned_data['mail']
            adresse = form.cleaned_data['adresse']
            motdepasse = form.cleaned_data['motdepasse']

            query = f"INSERT INTO user (nom, prenom, mail, adresse, motdepasse, statut) VALUES ('{nom}','{prenom}','{mail}','{adresse}','{make_password(motdepasse)}','client')"
            
            my_custom_sql(query)
           

        return HttpResponseRedirect('/login/')
    
    else:
        return render(request,"bubblemytea/index.html", context={"form":myForm})


def get_login(request):
    
    if request.method == "GET":
        return render(request,"bubblemytea/login.html", context={"form":login} )
    
    if request.method == "POST":
        check = True
        form = login(request.POST)
        
        if form.is_valid():
            mail = form.cleaned_data['mail']
            motdepasse = form.cleaned_data['motdepasse']
            query = f"SELECT * FROM user WHERE mail ='{mail}'"
            user: tuple[Any, ...] | None = my_custom_sql(query)

        
            if user != None:
           
                if check_password(motdepasse,user[5]) == True:
                    if user[8] == "client" :

                        encoded = jwt.encode({user[0]: "user_id"}, "secret", algorithm="HS256")
                        # decoded_data = jwt.decode(jwt=encoded,key='secret',algorithms='HS256')
                        response = redirect('dashboard/')
                        response.set_cookie('acces_tokken', encoded)   
                        return response
                    if user[8] == "admin" :

                        encoded = jwt.encode({user[0]: "user_id"}, "secret", algorithm="HS256")
                        # decoded_data = jwt.decode(jwt=encoded,key='secret',algorithms='HS256')
                        response = redirect('admin/')
                        response.set_cookie('acces_tokken', encoded)   
                        return response
                else:
                    return HttpResponseRedirect('/login/')
      
            else:
                return HttpResponseRedirect('/login/')
        else:

            return HttpResponseRedirect('/login/')
        

def my_custom_sql(query) -> tuple[Any, ...] | None:
    with connection.cursor() as cursor:
        cursor.execute(query)
        row: tuple[Any, ...] | None = cursor.fetchone()
    return row

def my_custom_sql2(query) -> tuple[Any, ...] | None:
    with connection.cursor() as cursor:
        cursor.execute(query)
        row: tuple[Any, ...] | None = cursor.fetchall()
    return row

def get_tokens_for_user(user) -> dict[str, str]:
    refresh = RefreshToken.for_user(user)
    return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),}  

def allproducts(request):
     request.method == 'GET'
     query = f"SELECT identifier, price, def FROM product"
     Allproducts = my_custom_sql2(query)
     

     return render(request,"product.html", context={"products":Allproducts})
