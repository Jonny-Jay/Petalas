# Generated by Django 4.2.5 on 2023-11-29 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0010_remove_presenca_crianca_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenca',
            name='crianca_nome',
            field=models.TextField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='presenca',
            name='presentes',
        ),
        migrations.AddField(
            model_name='presenca',
            name='presentes',
            field=models.BooleanField(default=False),
        ),
    ]