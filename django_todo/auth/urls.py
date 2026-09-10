
from . import views
from django.urls import path

urlpatterns = [
    path('',views.pagesac,name="acceuil"),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('ajouter_tache_personnel/<int:user_id>/', views.ajouter_tache_personnel, name='ajouter_tache_personnel'),
    path('taches_utilisateur/<int:user_id>/', views.les_taches_de_user, name='les_taches_de_user'),
]
