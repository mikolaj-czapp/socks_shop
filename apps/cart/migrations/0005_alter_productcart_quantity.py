# Generated by Django 3.2.6 on 2021-08-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210830_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]