# Generated by Django 2.2 on 2020-08-30 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]
