# Generated by Django 3.0.6 on 2020-05-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='status',
            field=models.CharField(default='Active', max_length=50),
        ),
    ]
