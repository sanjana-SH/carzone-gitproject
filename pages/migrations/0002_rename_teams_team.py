# Generated by Django 4.1.7 on 2023-03-25 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]