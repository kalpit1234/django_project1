# Generated by Django 4.2 on 2023-05-07 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_alter_reciepe_reciepe_view_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reciepe',
            old_name='reciepe_view_count',
            new_name='recipe_view_count',
        ),
    ]
