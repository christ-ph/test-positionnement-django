from django.contrib import admin
from django.urls import path
from . import views
from auth.views import *


urlpatterns = [
    # path('', views.liste_taches,name="liste_taches"),
    path("ajouter",views.ajouter_tache,name="ajouter_tache"),
    path("modifier/<int:id>/", views.modifie_tache, name="modifier_tache"),
    path("supprimer/<int:id>/", views.supprimer_tache, name="supprimer_tache"),
]