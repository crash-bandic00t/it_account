from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from ..models import Equipment
from ..forms import EquipmentForm, EquipmentUpdateForm


class EquipmentAddView(CreateView):
    model = Equipment
    template_name = 'main/equipment/equipment-add.html'
    form_class = EquipmentForm

    def get_success_url(self, **kwargs):
        import pdb
        pdb.set_trace()   
        return reverse_lazy('main:rack', args=[self.kwargs['autozal_slug'], self.kwargs['rack_number']])

class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'main/equipment/equipment-update.html'
    form_class = EquipmentUpdateForm
    context_object_name = 'equip'

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:rack', args=[self.kwargs['autozal_slug'], self.kwargs['rack_number']])


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'main/equipment/equipment-delete.html'
    context_object_name = 'equip'
    success_url = reverse_lazy('main:rack', )
    # import pdb
    # pdb.set_trace()

    def get_success_url(self, **kwargs):
        import pdb
        pdb.set_trace()       
        return reverse_lazy('main:rack', args=[self.])