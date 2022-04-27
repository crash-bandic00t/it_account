from ..models import Port

def ports_update(data, source_port):
    # если передается новый порт назначения
    if data.get('port'):
        dest_port = Port.objects.get(id=data.get('port'))
        # Редактируем порт назначения
        dest_port.busy = True
        dest_port.dest = str(source_port)
        dest_port.dest_port_id = source_port.id
        dest_port.desc = data.get('desc')           # описание и полный путь как у потра источника
        dest_port.full_path = data.get('full_path')
        dest_port.save()
        # Редактируем порт источник
        source_port.busy = True
        source_port.dest = str(dest_port)
        source_port.dest_port_id = dest_port.id     # описание и полный путь сохраняются из формы редактирования порта
        source_port.save()
    else:
        # пытаемся взять порт, если он уже был указан ранее
        try:
            dest_port = Port.objects.get(id=source_port.dest_port_id)
            dest_port.desc = data.get('desc')
            dest_port.full_path = data.get('full_path')
            dest_port.save()
        # если порт указан не был, и его не было ранее
        except:
            pass
