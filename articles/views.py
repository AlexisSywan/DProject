from .models import Auteur, Article
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ArticleForm


class DetailArticle(DetailView):
    model = Article


class ListeArticles(ListView):
    model = Article
    paginate_by = 50

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-date')
        return queryset


def home_view(request):
    last_article = Article.objects.all().order_by('-date')[:1]
    context = {
        'last_article': last_article
    }

    return render(request, 'accueil.html', context)


def accueil_article_view(request):
    article = Article.objects.latest('date')
    contexte = {
        'dernierArticle': article
    }
    return render(request, 'articles/accueil.html', contexte)


def accueil_id_view(request, idobjet):
    objmenu = Article.objects.only("titre")[:5]
    obj = Article.objects.get(id=idobjet)
    contexte = {
        'article': obj,
        'objmenu': objmenu
    }
    return render(request, 'articles/article_detail_view.html', contexte)


# def menuRecherche(request):
#     form = ArticleForm()
#     context = {'form': form}
#     return render(request, 'formulaire.html', context)

def form_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/formulaire.html', context)
