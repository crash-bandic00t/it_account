from django.http import JsonResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from ..models import Commutation, Equipment, Port, Rack
from ..forms import PortUpdateForm, DestinationPortUpdateForm
from ..functions.ports import ports_update


def port_update(request, pk):
    source_port = Port.objects.get(id=pk)
    source_port_form = PortUpdateForm(instance=source_port)
    dest_port_form = DestinationPortUpdateForm()
    if request.method == 'POST':
        source_port_form = PortUpdateForm(request.POST, instance=source_port)
        dest_port_form = DestinationPortUpdateForm(request.POST)
        if source_port_form.is_valid() and dest_port_form.is_valid():
            ports_update(request.POST, source_port)
            source_port_form.save()
            return redirect(
                'main:equipment-detail',
                autozal_slug=request.GET['autozal_slug'],
                rack_number=request.GET['rack_number'],
                place=request.GET['place'],
                )
    data = {
        'source_port_form': source_port_form,
        'dest_port_form': dest_port_form,
        'source_port': source_port
    }
    return render(request, 'main/ports/port-update.html', data)

def get_equip_dropdown(request):
    rack_id = request.GET.get('rack_id')
    equip = Equipment.objects.filter(rack_id=rack_id).order_by('place')
    return render(request, 'main/ports/equip-dropdown.html', {'equip': equip})

def get_port_dropdown(request):
    equip_id = request.GET.get('equip_id')
    ports = Port.objects.filter(equipment_id=equip_id).order_by('num')
    return render(request, 'main/ports/port-dropdown.html', {'ports': ports})

# def port_dest_update(request):
#     if request.method == 'POST':
#         form_port_dest = DestinationPortUpdateForm(request.POST)
#         print(1)
#         if form_port_dest.is_valid():
#             print('Валидна')
#     return redirect(
#                 'main:index',
#                 )
    # rack = Rack.objects.get(id=request.GET.get('rack_id'))
    # equip = Equipment.objects.get(id=request.GET.get('equip_id'))
    # port = Port.objects.get(id=request.GET.get('port_id'))
    # if port.busy:
    #     return JsonResponse({'error': True})
    # else:
    #     comm = Commutation.objects.get(source_port=port)
    #     comm.dest_port
    #     return JsonResponse({'success': True})


# class PortUpdateView(UpdateView):
#     model = Port
#     template_name = 'main/ports/port-update.html'
#     form_class = PortUpdateForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['ports'] = Port.objects.all()
#         return context

#     # вытаскиваем GET параметры с номером текущей стойки и slug автозала
#     def get_success_url(self, *args, **kwargs):
#         return reverse_lazy(
#             'main:equipment-detail',
#             args=[
#                 self.request.GET['autozal_slug'],
#                 self.request.GET['rack_number'],
#                 self.request.GET['place'],
#                 ]
#             )
    # def get_initial(self, **kwargs):
    #     initial = super(PortUpdateView, self).get_initial(**kwargs)
    #     initial['rack'] = Rack.objects.get(number=self.request.GET['rack_number'])
    #     return initial