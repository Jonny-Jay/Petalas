# Generated by Django 4.2.5 on 2023-10-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='entrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='status',
            field=models.TextField(max_length=255),
        ),
    ]