# Generated by Django 3.2.3 on 2021-11-21 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoeditor', '0005_auto_20211121_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='photooriginal',
            name='title',
        ),
    ]