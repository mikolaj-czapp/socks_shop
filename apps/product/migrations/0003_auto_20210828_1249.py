# Generated by Django 3.2.6 on 2021-08-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210828_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default='No brand', on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(default='No category', on_delete=django.db.models.deletion.SET_DEFAULT, to='product.category'),
        ),
    ]