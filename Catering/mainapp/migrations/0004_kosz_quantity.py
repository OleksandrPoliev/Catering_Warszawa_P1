# Generated by Django 3.2.9 on 2021-12-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_product_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='kosz',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]