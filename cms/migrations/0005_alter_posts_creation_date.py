# Generated by Django 4.1.7 on 2023-06-06 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_delete_pricehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]