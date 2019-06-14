from django.contrib import admin
from .models import Article
from .models import Categorie
from .models import Auteur

# Register your models here.
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Auteur)
