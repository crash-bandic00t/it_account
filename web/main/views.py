from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Autozal, Rack, Equipment
from .forms import EquipmentAddForm
from .validators import add_equipment_validator

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

# добавление нового оборудовния
def add_equipment(request, autozal_slug, rack_number):
    if request.method == 'POST':
        form = EquipmentAddForm(request.POST, request.FILES)
        if add_equipment_validator(request.POST):
            print('Валидация прошла')
        else:
            print('Валидация не пройдена')
    else:
        form = EquipmentAddForm()
    data = {
        'form': form,
    }
    return render(request, 'main/equipment-add.html', data)
