# Generated by Django 5.0.2 on 2024-02-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_one', models.IntegerField()),
                ('number_two', models.IntegerField()),
                ('answer', models.IntegerField()),
            ],
        ),
    ]