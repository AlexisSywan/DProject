from django.conf import settings
from articles.models import Categorie
from articles.models import Article


def menu(request):
    categories = Categorie.objects.all()
    articles = Article.objects.all().order_by('-date')[:5]
    objPrincipal = []

    # for category in categories:
    #     objPrincipal.append(category.nom)
    #     objPrincipal.append([articles.filter(category=category.id)])


    context = {
        'categories': categories,
        'articles': articles,
    }
    return context
