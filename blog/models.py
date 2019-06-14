from django.db import models
from datetime import datetime


class CartesMagic(models.Model):
    nom = models.CharField(max_length=100, default="")
    prix = models.DecimalField(decimal_places=2, max_digits=10000)
    image = models.CharField(max_length=10000, default="")
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.nom + " - " + str(self.prix) + " €"
