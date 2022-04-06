from mimetypes import init
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from ..models import Equipment, Rack
from ..forms import EquipmentForm, EquipmentUpdateForm

# добавление оборудования
class EquipmentAddView(CreateView):
    model = Equipment
    template_name = 'main/equipment/equipment-add.html'
    form_class = EquipmentForm

    # подставляем в форму номер стойки, из которой была нажата кнопка "Добавить"
    def get_initial(self, **kwargs):
        initial = super(EquipmentAddView, self).get_initial(**kwargs)
        initial['rack'] = Rack.objects.get(number=self.request.GET['rack_number'])
        return initial
    
    # вытаскиваем GET параметры с номером текущей стойки и slug автозала
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:rack',
            args=[
                self.request.GET['autozal_slug'],
                self.request.GET['rack_number']
                ]
            )

class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'main/equipment/equipment-update.html'
    form_class = EquipmentUpdateForm
    context_object_name = 'equip'

    # вытаскиваем GET параметры с номером текущей стойки и slug автозала
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:rack',
            args=[
                self.request.GET['autozal_slug'],
                self.request.GET['rack_number']
                ]
            )


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'main/equipment/equipment-delete.html'
    context_object_name = 'equip'

    # вытаскиваем GET параметры с номером текущей стойки и slug автозала
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:rack',
            args=[
                self.request.GET['autozal_slug'],
                self.request.GET['rack_number']
                ]
            )
               