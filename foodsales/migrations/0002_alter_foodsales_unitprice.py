# Generated by Django 4.1 on 2022-11-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodsales',
            name='unitprice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]