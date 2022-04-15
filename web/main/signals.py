from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Port, Equipment

# создает порты при создании нового оборудования
# обязательно в apps.py указать
# def ready(self): import main.signals
@receiver(post_save, sender=Equipment)
def create_ports(sender, instance, created, **kwargs):
    if created:
        for i in range(instance.port_cnt):
            Port.objects.create(
                equipment=instance,
                num=i+1,
            )