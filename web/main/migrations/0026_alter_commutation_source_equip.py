# Generated by Django 4.0.3 on 2022-04-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_commutation_source_equip_commutation_source_rack_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commutation',
            name='source_equip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_equip', to='main.equipment', verbose_name='Оборудование откуда '),
        ),
    ]
