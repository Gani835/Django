# Generated by Django 4.1 on 2022-11-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodsales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateField()),
                ('region', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('unitprice', models.IntegerField()),
            ],
        ),
    ]
