# Generated by Django 4.2 on 2023-04-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe',
            name='reciepe_image',
            field=models.ImageField(blank=True, upload_to='Recieps'),
        ),
    ]
