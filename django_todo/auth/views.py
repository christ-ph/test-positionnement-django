from django.shortcuts import get_object_or_404, render,redirect

from .models import *
from .forms import InscriptionForm, ConnexionForm
from todols.forms import Tachesforms
from todols.models import Tache


# Create your views here.

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            userid = form.cleaned_data['userid']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            confirmation = form.cleaned_data['confirmation']

            if mot_de_passe != confirmation:
                return render(request, 'auth/inscription.html', {'form': form, 'error': 'Les mots de passe ne correspondent pas.'})

            # Vérifier si l'utilisateur existe déjà
            if User.objects.filter(userid=userid).exists():
                return render(request, 'auth/inscription.html', {'form': form, 'error': 'Cet utilisateur existe déjà.'})

            # Créer un nouvel utilisateur
            user = User(nom=nom, prenom=prenom, userid=userid)
            user.set_password(mot_de_passe)  # Utiliser la méthode set_password pour hacher le mot de passe
            user.save()

            return redirect('les_taches_de_user', user_id=user.id)  
        form = InscriptionForm()

    return render(request, 'auth/inscription.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            try:
                user = User.objects.get(userid=userid)
                if user.check_password(mot_de_passe):
                    # Authentification réussie, rediriger vers la page de liste des tâches
                    return redirect('les_taches_de_user', user_id=user.id)
                else:
                    return render(request, 'auth/connexion.html', {'form': form, 'error': 'Mot de passe incorrect.'})
            except User.DoesNotExist:
                return render(request, 'auth/connexion.html', {'form': form, 'error': 'Utilisateur non trouvé.'})
    else:
        form = ConnexionForm()

    return render(request, 'auth/connexion.html', {'form': form})

def deconnexion(request):
    # Ici, vous pouvez gérer la déconnexion de l'utilisateur.
    # Par exemple, si vous utilisez des sessions, vous pouvez supprimer les informations de session.
    # Pour cet exemple, nous allons simplement rediriger vers la page de connexion.
    return redirect("connexion")


def ajouter_tache_personnel(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = Tachesforms(request.POST)
        if form.is_valid():
            # 1. Créer la tâche
            tache = form.save()  # enregistre directement

            # 2. Vérifier si l'association existe déjà (optionnel)
            if not TacheProprietaire.objects.filter(tache=tache, user=user).exists():
                # 3. Créer la liaison
                TacheProprietaire.objects.create(tache=tache, user=user)

            # 4. Rediriger vers la liste des tâches de l'utilisateur
            return redirect('les_taches_de_user', user_id=user.id)
    else:
        # Méthode GET : afficher un formulaire vide
        form = Tachesforms()

    # Rendu du formulaire (GET ou formulaire invalide)
    return render(request, 'tache/formtache.html', {'form': form, 'user_cible': user})

def les_taches_de_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    taches = Tache.objects.filter(tacheproprietaire__user=user)
    return render(request, 'tache/list.html', {'taches': taches, 'user': user})

def pagesac(request):

    return render(request,"auth/acceuil.html")
