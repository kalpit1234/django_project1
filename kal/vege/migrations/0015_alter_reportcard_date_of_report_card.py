# Generated by Django 4.2 on 2023-05-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0014_alter_reportcard_date_of_report_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card',
            field=models.DateField(auto_now_add=True),
        ),
    ]
