# Generated by Django 4.1 on 2022-09-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewProject', '0002_createuser_username_alter_createuser_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuicesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JuiceId', models.CharField(max_length=20)),
                ('JuiceName', models.CharField(max_length=20)),
            ],
        ),
    ]
