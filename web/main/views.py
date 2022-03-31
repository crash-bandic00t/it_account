from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Autozal, Rack, Equipment
from .forms import EquipmentAddForm

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
class EquipmentAddView(CreateView):
    model = Equipment
    form_class = EquipmentAddForm
    template_name = 'main/equipment-add.html'
    success_url = reverse_lazy('main:index')
