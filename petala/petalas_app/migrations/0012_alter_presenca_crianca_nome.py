# Generated by Django 4.2.5 on 2023-11-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0011_presenca_crianca_nome_remove_presenca_presentes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='crianca_nome',
            field=models.TextField(),
        ),
    ]
