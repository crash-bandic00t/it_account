# Generated by Django 4.0.3 on 2022-04-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_commutation_dest_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='dest',
            field=models.CharField(default='-', max_length=100, verbose_name='Куда'),
        ),
    ]