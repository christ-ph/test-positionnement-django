from django.shortcuts import render,get_object_or_404,redirect
from .forms import Tachesforms


from .models import *

# Create your views here.
def liste_taches(request):
    filtre = request.GET.get('status', 'toutes')
    taches = Tache.objects.all()

    if filtre == 'en_cours':
        taches = taches.filter(status=Tache.Status.PENDING)
    elif filtre == 'terminees':
        taches = taches.filter(status=Tache.Status.DONE)

    return render(request, "tache/list.html", {"taches": taches, "filtre": filtre})


def ajouter_tache(request):

    form = Tachesforms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('liste_taches')
    return render(request,"tache/formtache.html",{"form":form})

def modifie_tache(request,id):
    tache = get_object_or_404(Tache,id=id)

    form = Tachesforms(request.POST or None,instance=tache)

    if form.is_valid():
        form.save()
        return redirect('liste_taches')
    return render(request,"tache/formtache.html",{"form":form})


def supprimer_tache(request, id):
    tache = get_object_or_404(Tache, id=id)
    if request.method == "POST":
        tache.delete()
        return redirect('liste_taches')

    return render(request, 'tache/supprimer_tache.html', {'tache': tache})

    

