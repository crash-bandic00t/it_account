from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from ..models import Port
from ..forms import PortUpdateForm


class PortUpdateView(UpdateView):
    model = Port
    template_name = 'main/ports/port-update.html'
    form_class = PortUpdateForm
    context_object_name = 'equip'

    # вытаскиваем GET параметры с номером текущей стойки и slug автозала
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:equipment-detail',
            args=[
                self.request.GET['autozal_slug'],
                self.request.GET['rack_number'],
                self.request.GET['place'],
                ]
            )

