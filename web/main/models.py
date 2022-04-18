from email.policy import default
from django.db import models

from pytils.translit import slugify


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
    )

    class Meta:
        db_table = 'equipment'
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        unique_together = ['rack', 'place']

    type = models.CharField('Тип оборудования', max_length=100, choices=EQUPMENT_TYPES, blank=True)
    rack = models.ForeignKey(Rack, verbose_name='Стойка', related_name='equipment', on_delete=models.CASCADE)
    place = models.CharField('Место', max_length=5)
    name = models.CharField('Наименование', max_length=100)
    owner = models.CharField('Владелец', max_length=50)
    desc = models.CharField('Описание', max_length=500, blank=True)
    port_cnt = models.PositiveIntegerField('Количество портов')
    def __str__(self):
        return (f'{self.place} {self.name}')


class Category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return (f'{self.name}')



class Port(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='ports', on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, verbose_name='Оборудование', related_name='ports', on_delete=models.CASCADE)
    type = models.CharField('Тип порта', max_length=6, default='access')
    vlan = models.CharField('Vlan', max_length=100, default=999)
    num = models.PositiveIntegerField('№ порта')
    busy = models.BooleanField('Порт занят', default=False)
    active = models.BooleanField('Порт включен', default=False)
    dest = models.CharField('Куда', max_length=100, blank=True)
    dest_port_id = models.PositiveIntegerField('ID порта назначения', blank=True, null=True)
    full_path = models.CharField('Полный путь', max_length=100, default='-', blank=True)
    desc = models.CharField('Описание', max_length=100, default='-')

    class Meta:
        db_table = 'port'
        verbose_name = 'Порт'
        verbose_name_plural = 'Порты'
    
    def __str__(self):
        return (f'{self.equipment.rack.number}-{self.equipment.place}-{self.num}')
