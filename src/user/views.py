from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import redirect
from bubblemytea.views import my_custom_sql, my_custom_sql2
from .models import User
from .form import modif
import jwt

date =datetime.today()

def get_dashboard(request):
   
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        # print(test[0])
        query = f"SELECT * FROM user WHERE id ='{test[0]}'"
        user = my_custom_sql(query)

        query = f"SELECT identifier, price, def FROM product"
        Allproducts = my_custom_sql2(query)

        
        # query= f"SELECT * from product"
        # product = my_custom_sql2(query)
        
        # identifier, price, def
        return render(request,"user/dashboard.html",context= {"prenom":user[3],"date":date,"products":Allproducts})


def get_profil(request):
   
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        # print(test[0])
        query = f"SELECT * FROM user WHERE id ='{test[0]}'"
        user = my_custom_sql(query)
   
        return render(request,"user/profil.html",context= {"prenom":user[3],"nom":user[2],"mail":user[1],"adresse":user[4],"motdepasse":user[5],"modif":modif})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        query = f"SELECT * FROM user WHERE id ='{test[0]}'"
        user = my_custom_sql(query)

        formmodif = modif(request.POST)
        print(formmodif.is_valid())
        if formmodif.is_valid():
            
            nom = formmodif.cleaned_data['nom']
            prenom = formmodif.cleaned_data['prenom']
            mail = formmodif.cleaned_data['mail']
            adresse = formmodif.cleaned_data['adresse']
            motdepasse = formmodif.cleaned_data['motdepasse']
        
            query = f"UPDATE user set nom='{nom}', prenom='{prenom}', mail='{mail}', adresse='{adresse}', motdepasse='{make_password(motdepasse)}' where id= '{user[0]}'"
            my_custom_sql(query)
            return render(request,"user/profil.html",context= {"prenom":user[3],"nom":user[2],"mail":user[1],"adresse":user[4],"motdepasse":user[5],"modif":formmodif})
        

def get_commande(request):
   
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        # print(test[0])
        query = f"SELECT * FROM user WHERE id ='{test[0]}'"
        user = my_custom_sql(query)
        return render(request,"user/commande.html",context= {"prenom":user[3],"date":date})  
   




# Create your views here.
def get_form(request):
    if request.method == "GET":
        return render(request,"register.html", context={"form":myForm})
 
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
        return render(request,"index.html", context={"form":myForm})


def get_login(request):
    if request.method == "GET":
        return render(request,"login.html", context={"form":login})
    
    if request.method == "POST":
        form = login(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            motdepasse = form.cleaned_data['motdepasse']

            #query = f"SELECT * FROM user WHERE mail ='{mail}' and motdepasse ='{check_password(motdepasse)}'"
            query = f"SELECT * FROM user WHERE mail ='{mail}'"
            user = my_custom_sql(query)
            if check_password(motdepasse,user[5]) == True:

                return render(request,"test.html")

            else:
                return render(request,"index.html", context={"form":myForm})
        else:
            return render(request,"index.html", context={"form":myForm})
        

def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()
    return row

def my_custom_sql2(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row
