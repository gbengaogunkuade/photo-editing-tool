# Generated by Django 3.2.3 on 2021-11-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoeditor', '0002_delete_photodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoOriginal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session_id', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(default='default.jpg', upload_to='original_images/')),
            ],
            options={
                'verbose_name_plural': 'PhotoOriginal',
            },
        ),
    ]
