# Generated by Django 4.1 on 2022-09-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createuser',
            name='UserName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createuser',
            name='FirstName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]