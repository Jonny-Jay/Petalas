# Generated by Django 4.2.5 on 2023-11-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0008_presenca_crianca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenca',
            name='crianca',
        ),
        migrations.AddField(
            model_name='presenca',
            name='crianca_nome',
            field=models.TextField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
