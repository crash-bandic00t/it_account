# Generated by Django 4.0.3 on 2022-04-14 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_remove_port_commutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='main.category', verbose_name='Категория'),
        ),
    ]
