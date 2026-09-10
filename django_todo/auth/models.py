from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class User(models.Model):

    nom = models.CharField(max_length=100, blank=True,name="nom")
    prenom = models.CharField(max_length=100, blank=True,name="prenom")
    userid = models.CharField(max_length=100, unique=True,name="userid")
    mot_de_passe = models.CharField(max_length=100, blank=True,name="mot_de_passe")

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def set_password(self, raw_password):
        self.mot_de_passe = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.mot_de_passe)
    
class TacheProprietaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
    tache = models.ForeignKey('todols.Tache', on_delete=models.CASCADE, name="tache")

    class Meta:
        unique_together = ('user', 'tache')

    def __str__(self):
        return f"{self.user} - {self.tache}"
