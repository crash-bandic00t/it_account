from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Port, Equipment, Vlan, Complex

# создает порты при создании нового оборудования
# обязательно в apps.py указать
# def ready(self): import main.signals
@receiver(post_save, sender=Equipment)
def create_ports(sender, instance, created, **kwargs):
    if created:
        for i in range(instance.port_cnt):
            obj = Port.objects.create(
                equipment=instance,
                name=f'{instance.prefix}{i+1}',
                num=i+1,
            )
            # добавляем на каждый порт оборудования дефолтный vlan 999
            if instance.type == 'active':
                obj.vlan.add(Vlan.objects.get(vlan_id=999, complex=instance.complex))

# создание vlan 999 для каждого комплекса по умолчанию
@receiver(post_save, sender=Complex)
def create_vlan_999(sender, instance, created, **kwargs):
    if created:
        Vlan.objects.create(
            complex=instance,
            vlan_id=999,
            name='free'
            )