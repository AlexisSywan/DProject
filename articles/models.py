from django.db import models
from datetime import datetime


class Auteur(models.Model):
    nom = models.CharField(max_length=100, default="")
    prenom = models.CharField(max_length=100, default="")
    dateNaissance = models.DateField(default=datetime.now)
    pseudo = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.pseudo


class Categorie(models.Model):
    nom = models.CharField(max_length=100, default="")
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100, default="")
    contenu = models.CharField(max_length=10000, default="")
    date = models.DateTimeField(default=datetime.now)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.titre + ' - ' + self.contenu + ' - ' + str(self.category) + '-' + str(self.id)
