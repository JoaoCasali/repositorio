# Generated by Django 4.1.7 on 2023-03-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='bairro',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='comentario',
            name='cep',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='comentario',
            name='cidade',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='comentario',
            name='complemento',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='rua',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='comentario',
            name='uf',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
