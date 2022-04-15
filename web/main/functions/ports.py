from ..models import Commutation, Equipment, Port, Rack

def ports_update(data, source_port):
    try:
        dest_port = Port.objects.get(id=data.get('port'))
        dest_port.dest = str(source_port)
        dest_port.busy = True
        dest_port.dest_port_id = source_port.id
        dest_port.desc = data.get('desc')
        dest_port.full_path = data.get('full_path')
        if not dest_port.active:
            dest_port.active = True
        dest_port.save()
        source_port.dest = str(dest_port)
        source_port.busy = True
        source_port.dest_port_id = dest_port.id
        source_port.save()
    except:
        dest_port = Port.objects.get(id=source_port.dest_port_id)
        dest_port.desc = data.get('desc')
        dest_port.full_path = data.get('full_path')
    