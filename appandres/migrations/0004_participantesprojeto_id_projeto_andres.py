# Generated by Django 4.2 on 2025-02-07 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appandres', '0003_alter_participantesprojeto_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantesprojeto',
            name='id_projeto_andres',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appandres.projetosandres'),
            preserve_default=False,
        ),
    ]
