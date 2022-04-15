# Generated by Django 4.0.3 on 2022-04-12 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_commutation_dest_equip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commutation',
            name='source_equip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_equip', to='main.port', verbose_name='Оборудование откуда '),
        ),
        migrations.AddField(
            model_name='commutation',
            name='source_rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_rack', to='main.rack', verbose_name='Стойка откуда '),
        ),
        migrations.AlterField(
            model_name='commutation',
            name='source_port',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_port', to='main.port', verbose_name='Порт откуда'),
        ),
    ]
