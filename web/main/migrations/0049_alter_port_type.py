# Generated by Django 4.0.3 on 2022-04-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_remove_port_vlan_port_vlan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='type',
            field=models.CharField(choices=[('', 'Выберите тип...'), ('a', 'Access'), ('t', 'Trunk')], default='a', max_length=1, verbose_name='Тип порта'),
        ),
    ]
