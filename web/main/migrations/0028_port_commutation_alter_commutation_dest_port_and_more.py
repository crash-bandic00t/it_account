# Generated by Django 4.0.3 on 2022-04-12 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_remove_commutation_dest_equip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='commutation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='main.commutation', verbose_name='Коммутация'),
        ),
        migrations.AlterField(
            model_name='commutation',
            name='dest_port',
            field=models.CharField(default='-', max_length=10, verbose_name='Куда'),
        ),
        migrations.AlterField(
            model_name='commutation',
            name='source_port',
            field=models.CharField(default='-', max_length=10, verbose_name='Откуда'),
        ),
    ]
