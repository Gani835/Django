# Generated by Django 4.1 on 2022-09-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('EmailAddress', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('ConfirmPassword', models.CharField(max_length=20)),
            ],
        ),
    ]
