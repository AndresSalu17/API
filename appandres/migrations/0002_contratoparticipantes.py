# Generated by Django 4.2 on 2025-02-12 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appandres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContratoParticipantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo')])),
                ('resumo', models.CharField(max_length=150)),
                ('id_projeto_andres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appandres.projetosandres')),
            ],
            options={
                'db_table': 'contrato_participantes',
            },
        ),
    ]
