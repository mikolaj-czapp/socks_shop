

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='cart',
        ),
    ]
