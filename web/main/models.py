from email.policy import default
from django.db import models
from pkg_resources import require

from pytils.translit import slugify


class Complex(models.Model):
    name = models.CharField('Наименование комплекса', max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        db_table = 'complex'
        verbose_name = 'Комплекс'
        verbose_name_plural = 'Комплексы'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.name}')


class Vlan(models.Model):
    
    class Meta:
        db_table = 'vlan'
        verbose_name = 'Vlan'
        verbose_name_plural = 'Vlans'
        unique_together = ['vlan_id', 'complex']

    vlan_id = models.PositiveIntegerField(verbose_name='Номер vlan')
    name = models.CharField('Наименование vlan', max_length=100)
    complex = models.ForeignKey(Complex, verbose_name='Комплекс', related_name='vlan', on_delete=models.CASCADE)

    def __str__(self):
        return (f'Vlan {self.vlan_id}')

class Autozal(models.Model):
    class Meta:
        db_table = 'cas'
        verbose_name = 'Автозал'
        verbose_name_plural = 'Автозалы'
    name = models.CharField('Наименование', max_length=10)
    floor = models.PositiveIntegerField(verbose_name='Этаж', blank=True)
    desc = models.TextField('Описание', max_length=500, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    # превращаем имя автозала в slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.name}')


class Rack(models.Model):
    class Meta:
        db_table = 'rack'
        verbose_name = 'Стойка'
        verbose_name_plural = 'Стойки'
    autozal = models.ForeignKey(Autozal, verbose_name='Автозал', related_name='racks', on_delete=models.CASCADE)
    number = models.PositiveIntegerField('Номер', unique=True)
    desc = models.TextField('Описание', max_length=500, blank=True, default='-')

    def __str__(self):
        return (f'ТШ {self.number}')

class Equipment(models.Model):
    EQUPMENT_TYPES = (
        ('', 'Выберите тип...'),
        ('active','Активное оборудование'),
        ('passive', 'Пассивное оборудование'),
        ('server', 'Сервер'),
        ('unmanageable', 'Неуправляемое оборудование'),
        ('operator', 'Оборудование оператора связи'),
    )

    class Meta:
        db_table = 'equipment'
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        unique_together = ['rack', 'place']

    complex = models.ForeignKey(Complex, verbose_name='Комплекс', related_name='equipment', on_delete=models.CASCADE, null=True)
    type = models.CharField('Тип оборудования', max_length=100, choices=EQUPMENT_TYPES, blank=True)
    rack = models.ForeignKey(Rack, verbose_name='Стойка', related_name='equipment', on_delete=models.CASCADE)
    place = models.CharField('Место', max_length=5)
    name = models.CharField('Наименование', max_length=100)
    owner = models.CharField('Владелец', max_length=50)
    desc = models.TextField('Описание', max_length=500, blank=True)
    prefix = models.CharField('Префикс порта', max_length=15, blank=True, null=True)
    port_cnt = models.PositiveIntegerField('Количество портов')

    def __str__(self):
        return (f'{self.place} {self.name}')


class Port(models.Model):
    PORT_TYPES = (
            ('', 'Выберите тип...'),
            ('access','Access'),
            ('trunk', 'Trunk'),
        )

    equipment = models.ForeignKey(Equipment, verbose_name='Оборудование', related_name='ports', on_delete=models.CASCADE)
    type = models.CharField('Тип порта', max_length=6, choices=PORT_TYPES, default='access')
    vlan = models.ManyToManyField(Vlan, blank=True)
    name = models.CharField('Наименование порта', max_length=20, null=True)
    num = models.PositiveIntegerField('Номер порта', blank=True, null=True)
    busy = models.BooleanField('Порт занят', default=False)
    active = models.BooleanField('Порт включен', default=False)
    dest = models.CharField('Куда', max_length=100, blank=True, default='-')
    dest_port_id = models.PositiveIntegerField('ID порта назначения', blank=True, null=True)
    full_path = models.CharField('Полный путь', max_length=100, default='-', blank=True)
    desc = models.TextField('Описание', max_length=500, blank=True, default='-')

    class Meta:
        db_table = 'port'
        verbose_name = 'Порт'
        verbose_name_plural = 'Порты'
    
    def __str__(self):
        return (f'{self.equipment.rack.number}-{self.equipment.place}-{self.num}')

