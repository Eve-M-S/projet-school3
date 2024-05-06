from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import connection
from user.views import my_custom_sql,my_custom_sql2
from django.contrib.auth.hashers import make_password, check_password
import jwt
from .form import create_product, create_User, update_User, remove_product, Update_product,remove_user
from datetime import datetime
date =datetime.today()

# Ajout d'un user via un compte admin 
def get_admin(request):
   
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        # print(test[0])
        query = f"SELECT * FROM user WHERE id ='{test[0]}'"
        user = my_custom_sql(query)

        query = f"SELECT identifier, price, def FROM product"
        Allproducts = my_custom_sql2(query)

        return render(request,"administrator/admin.html",context= {"prenom":user[3],"date":date,"products":Allproducts})


def add_user(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/add_user.html", context={"form":create_User})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = create_User(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            mail = form.cleaned_data['mail']
            adresse = form.cleaned_data['adresse']
            statut = form.cleaned_data['statut']
            motdepasse = form.cleaned_data['motdepasse']
        
            query = f"INSERT INTO user (nom, prenom, mail, adresse, statut, motdepasse) VALUES ('{nom}','{prenom}','{mail}','{adresse}','{statut}','{make_password(motdepasse)}','client')"

            my_custom_sql(query)

        return HttpResponseRedirect('/admin/')
    
    else:
        return render(request,"admin.html", context={"form":create_User})

def update_user(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/update_user.html", context={"form":update_User})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = update_User(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            mail = form.cleaned_data['mail']
            adresse = form.cleaned_data['adresse']
            statut = form.cleaned_data['statut']
            motdepasse = form.cleaned_data['motdepasse']

            query = f"SELECT * FROM user WHERE mail ='{mail}'"

            user = my_custom_sql(query)

            if user != None:
                query = f"UPDATE user set nom='{nom}', prenom='{prenom}', mail='{mail}', adresse='{adresse}', motdepasse='{make_password(motdepasse)}', statut='{statut}' where id= '{user[0]}'"
                my_custom_sql(query)
            else:
                return HttpResponseRedirect('/login/admin/update_user/')
        else:
            return HttpResponseRedirect('/login/admin/update_user/')

        return HttpResponseRedirect('/login/admin/update_user/')
    
    else:
        return render(request,"up.html", context={"form":update_User})

# Ajout des produits depuis compte admin dans la BdD
def addproducts(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/add_product.html", context={"form":create_product})
    
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = create_product(request.POST)
        if form.is_valid():
            identifier= form.cleaned_data['identifier']
            prix = form.cleaned_data['prix']
            description = form.cleaned_data['description']
            stock= form.cleaned_data['stock']
            
        
            query = f"INSERT INTO product (identifier, price, def, stock) VALUES ('{identifier}','{prix}','{description}','{stock}')"

            my_custom_sql(query)
            return render(request,"administrator/add_product.html",context={"form":create_product})
        
    
    else:
        return render(request,"administrator/add_product.html", context={"form":create_product})
    
# Supprimer un produit 
def deleteproducts(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/remove_product.html", context={"form":remove_product})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = remove_product(request.POST)
        if form.is_valid():
            identifier= form.cleaned_data['identifier']

            query = f"SELECT * FROM product WHERE identifier ='{identifier}'"
            product =my_custom_sql(query)

            if product != None:

                query = f"DELETE FROM product WHERE id = '{product[0]}' "
                my_custom_sql(query)

                return HttpResponseRedirect('/login/admin/remove_product/')

            else:
                return HttpResponseRedirect('/login/admin/remove_product/')
    else:
        return render(request,"product.html", context={"form":remove_product})


def updateproducts(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/update_product.html", context={"form":Update_product})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = Update_product(request.POST)
        if form.is_valid():
            
            identifier= form.cleaned_data['identifier']
            price = form.cleaned_data['prix']
            description = form.cleaned_data['description']
            stock= form.cleaned_data['stock']


            query = f"SELECT * FROM product WHERE identifier ='{identifier}'"

            product= my_custom_sql(query)

            if product != None:  
                query = f"UPDATE product SET identifier='{identifier}', price='{price}', def='{description}', stock='{stock}' WHERE identifier='{identifier}'"   
            
                my_custom_sql(query)

            
            return HttpResponseRedirect('/login/admin/update_product/')
                 
        else:
            return HttpResponseRedirect('/login/admin/update_product/')
        
        # return HttpResponseRedirect('/')
    else:    
        return render(request,"administrator/update_product.html", context={"form":Update_product})
          
def deleteuser(request):
    if request.method == "GET":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        return render(request,"administrator/remove_user.html", context={"form":remove_user})
    if request.method == "POST":
        cookie  = request.COOKIES['acces_tokken']
        decoded_data = jwt.decode(jwt=cookie,key='secret',algorithms='HS256')
        test = list(decoded_data)
        form = remove_user(request.POST)
        if form.is_valid():
           
            mail = form.cleaned_data['mail']

            query = f"SELECT * FROM user WHERE mail ='{mail}'"

            user= my_custom_sql(query)

            if user != None:  
                query = f"DELETE FROM user WHERE id = '{user[0]}' "

                my_custom_sql(query)
                return HttpResponseRedirect('login/admin/remove_user/')
            else:
                return HttpResponseRedirect('/login/admin/remove_user/')   
        else:
            return render(request,"admin.html", context={"form":remove_user})
