# Generated by Django 4.2 on 2023-04-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciepe_name', models.CharField(max_length=123)),
                ('reciepe_description', models.TextField()),
                ('reciepe_image', models.ImageField(upload_to='Recieps')),
            ],
        ),
    ]
