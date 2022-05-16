# Generated by Django 4.0.3 on 2022-05-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_alter_equipment_port_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='desc',
            field=models.TextField(blank=True, max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='type',
            field=models.CharField(blank=True, choices=[('', 'Выберите тип...'), ('active', 'Активное оборудование'), ('passive', 'Пассивное оборудование'), ('unmanageable', 'Неуправляемое оборудование'), ('operator', 'Оборудование оператора связи')], max_length=100, verbose_name='Тип оборудования'),
        ),
    ]
