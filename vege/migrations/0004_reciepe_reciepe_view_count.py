# Generated by Django 4.2 on 2023-05-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_reciepe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepe',
            name='reciepe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]