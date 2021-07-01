from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def projects(request):
    return render(request, 'main/projects.html')


def contacts(request):
    return render(request, 'main/conts.html')