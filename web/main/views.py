from django.shortcuts import render


def index(request):
    return render(request, 'main/blank.html', context={
        'title': 'Главная'
    })