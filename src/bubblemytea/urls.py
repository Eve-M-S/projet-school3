"""
URL configuration for bubblemytea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from .views import get_form, get_login,allproducts
from user.views import get_profil,get_dashboard, get_commande
from administrator.views import addproducts, add_user,update_user, deleteproducts, updateproducts,get_admin,deleteuser

urlpatterns = [
    #path('',index, name="index"),
    path('',get_form, name="get_form"),
    # path('admin/', admin.site.urls),
    path('login/', get_login, name="get_login" ),


    path('login/dashboard/', get_dashboard, name="get_profil"),
    path('login/dashboard/profil/', get_profil, name="get_profil"),
    path('login/dashboard/commandes/',get_commande, name="get_commande"),
    

    path('login/admin/',get_admin, name="get_admin"),

    path('login/admin/add_product/', addproducts, name ="add_product"),
    path('login/admin/remove_product/', deleteproducts, name ="remove_product"),
    path('login/admin/update_product/', updateproducts, name ="update_product"),
    path('login/admin/add_user/', add_user, name ="add_user"),
    path('login/admin/update_user/', update_user, name ="update_user"),
    path('login/admin/remove_user/', deleteuser, name ="remove_user"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('setcookie', setcookie),
    # path('getcookie', showcookie),
]

