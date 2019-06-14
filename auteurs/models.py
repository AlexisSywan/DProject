from django.db import models
from datetime import datetime


class Auteur(models.Model):
    nom = models.CharField(max_length=100, default="")
    prenom = models.CharField(max_length=100, default="")
    dateNaissance = models.DateField(default=datetime.now)
    pseudo = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nom
