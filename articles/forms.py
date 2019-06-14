from django import forms
from .models import Article as ArticleModel


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = [
            'titre',
            'contenu',
            'date',
            'auteur',
            'category'
        ]
