from django.db import models

# Create your models here.
class Tache(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING" , "En cours"
        DONE = "DONE" , "Terminee"
    class Priorite(models.TextChoices):
        BASE = "BASE" , "Base"
        MOYENNE = "MOYENNE" , "Moyenne"
        HAUTE = "HAUTE","Haute"
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(
        max_length = 10,
        choices = Status.choices,
        default = Status.PENDING
    )
    priorite = models.CharField(
        max_length = 10,
        choices = Priorite.choices,
        default = Priorite.MOYENNE
        
    )
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre
        
        

