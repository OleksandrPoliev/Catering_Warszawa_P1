# Generated by Django 3.2.9 on 2021-12-07 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_rename_quantity_orderitem_ilość'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Imie',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Nazwisko',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]