
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('index',views.index),
    path('',views.base),
    path("registration",views.registration),
    path("login",views.login),
    path("home",views.home),
    path("logout",views.logout),
    path("afterlogin",views.afterlogin),


    # path("mysession",views.mysession),
    # path("sessionset",views.sessionset),
    # path("sessionremove",views.sessionremove),
    # path("sessionview",views.sessionview),

]
