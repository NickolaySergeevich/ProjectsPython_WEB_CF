# Generated by Django 5.0.2 on 2024-02-23 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0002_alter_phonebook_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonebook',
            old_name='contact_notes',
            new_name='contact_note',
        ),
    ]
