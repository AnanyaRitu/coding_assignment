# Generated by Django 4.2.1 on 2023-05-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='customer_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product_id',
            field=models.CharField(max_length=255),
        ),
    ]
