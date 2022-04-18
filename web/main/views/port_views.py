from django.http import JsonResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from ..models import Equipment, Port, Rack
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

def port_clear(request):
    # берем порт источник
    source_port = Port.objects.get(id=request.GET.get('source_port_id'))
    # пытаемся взять порт назначения
    try:
        dest_port = Port.objects.get(id=request.GET.get('dest_port_id'))
    except:
        dest_port = None
    source_port.busy = False
    source_port.dest = ''
    source_port.dest_port_id = None
    source_port.full_path = ''
    source_port.desc = '-'
    source_port.save()
    if dest_port:
        dest_port.busy = False
        dest_port.dest = ''
        dest_port.dest_port_id = None
        dest_port.full_path = ''
        dest_port.desc = '-'
        dest_port.save()

    return redirect(request.META['HTTP_REFERER'])

def get_equip_dropdown(request):
    rack_id = request.GET.get('rack_id')
    equip = Equipment.objects.filter(rack_id=rack_id).order_by('place')
    return render(request, 'main/ports/equip-dropdown.html', {'equip': equip})

def get_port_dropdown(request):
    equip_id = request.GET.get('equip_id')
    ports = Port.objects.filter(equipment_id=equip_id).order_by('num')
    return render(request, 'main/ports/port-dropdown.html', {'ports': ports})