# Generated by Django 4.2.5 on 2023-11-30 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0012_alter_presenca_crianca_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doacao',
            old_name='descricao',
            new_name='destino',
        ),
        migrations.RenameField(
            model_name='doacao',
            old_name='nome_crianca',
            new_name='tipo',
        ),
    ]
