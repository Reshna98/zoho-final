# Generated by Django 4.2.2 on 2024-05-04 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_remove_payment_made_bills_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_made',
            old_name='source_of_supply_of_supply',
            new_name='source_of_supply',
        ),
    ]
