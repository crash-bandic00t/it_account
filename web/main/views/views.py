from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from ..models import Autozal, Commutation, Port, Rack, Equipment

#главная страница
def index(request):
    autozals = Autozal.objects.all()
    return render(request, 'main/index.html', context={
        'title': 'Главная',
        'autozals': autozals
    })

# стойки в указанном автозале
def autozal(request, autozal_slug):
    autozal = Autozal.objects.get(slug=autozal_slug)
    data = {
        'autozal': autozal
    }
    return render(request, 'main/autozal.html', data)

# содержимое стойки
def rack(request, autozal_slug, rack_number):
    rack = Rack.objects.get(number=rack_number)
    data = {
        'rack': rack
    }
    return render(request, 'main/rack.html', data)

# порты на оборудовании
def equipment(request, autozal_slug, rack_number, place):
    rack = Rack.objects.get(number=rack_number)
    equipment = Equipment.objects.get(place=place, rack=rack)
    data = {
        'rack': rack,
        'equipment': equipment,
    }
    return render(request, 'main/equipment/equipment-detail.html', data)

# все коммутации
def commutation(request):
    comm = Commutation.objects.all()
    data = {
        'commutations': comm
    }
    return render(request, 'main/commutation.html', data)