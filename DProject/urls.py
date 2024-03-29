"""DProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import purBeurreStyleGuide_view
from blog.views import uiLibrary_view
from blog.views import templates_view
from articles.views import accueil_article_view


urlpatterns = [
    path('article/', include('articles.urls')),
    path('', accueil_article_view, name="home"),
    path('ui-library/', uiLibrary_view, name="uiLibrary"),
    path('templates/', templates_view, name="templates"),
    path('admin/', admin.site.urls),
]
