from os import pread
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from ..models import Complex, Vlan
from ..forms.vlan_forms import VlanForm, VlanUpdateForm


def vlan(request, complex):
    complex = Complex.objects.get(slug=complex)
    return render(request, 'main/vlan/vlan.html', context={
        'complex': complex
    }) 

# добавление влана
class VlanAddView(CreateView):
    model = Vlan
    template_name = 'main/vlan/vlan-add.html'
    form_class = VlanForm

    # подставляем в форму номер стойки, из которой была нажата кнопка "Добавить"
    def get_initial(self, **kwargs):
        print(self.request.GET)
        initial = super(VlanAddView, self).get_initial(**kwargs)
        initial['complex'] = Complex.objects.get(slug=self.request.GET['complex_slug'])
        return initial
    
    # вытаскиваем GET параметры с номером текущей стойки и slug автозала
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:vlan',
            args=[
                self.request.GET['complex_slug'],
                ]
            )


# редактирование Vlan
class VlanUpdateView(UpdateView):
    model = Vlan
    template_name = 'main/vlan/vlan-update.html'
    form_class = VlanUpdateForm
    context_object_name = 'vlan'

    # вытаскиваем GET параметры со slug комплекса
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:vlan',
            args=[
                self.request.GET['complex_slug'],
                ]
            )


# удаление vlan
class VlanDeleteView(DeleteView):
    model = Vlan
    template_name = 'main/vlan/vlan-delete.html'
    context_object_name = 'vlan'

    # вытаскиваем GET параметры со slug комплекса
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'main:vlan',
            args=[
                self.request.GET['complex_slug'],
                ]
            )
