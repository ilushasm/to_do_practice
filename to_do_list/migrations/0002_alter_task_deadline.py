# Generated by Django 4.2.2 on 2023-06-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
