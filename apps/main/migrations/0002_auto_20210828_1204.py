# Generated by Django 3.2.6 on 2021-08-28 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='productcart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='productcart',
            name='items',
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCart',
        ),
    ]
