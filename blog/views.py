from django.shortcuts import render


def purBeurreStyleGuide_view(request):
    return render(request, 'purBeurreStyleGuide.html', {})


def uiLibrary_view(request):
    return render(request, 'uiLibrary.html', {})


def templates_view(request):
    return render(request, 'templates.html', {})
