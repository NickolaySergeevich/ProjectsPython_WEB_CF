# Generated by Django 5.0.2 on 2024-02-23 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_header', models.TextField()),
                ('note_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotesSupplements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_supplement', models.TextField()),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.notes')),
            ],
        ),
    ]