# Generated by Django 4.2.5 on 2023-11-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id_doacao', models.AutoField(primary_key=True, serialize=False)),
                ('nome_padrinho', models.TextField(max_length=255)),
                ('valor', models.IntegerField()),
                ('nome_crianca', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
            ],
        ),
    ]
