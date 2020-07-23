# Generated by Django 3.0.8 on 2020-07-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='result',
            field=models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], max_length=20, verbose_name='Qual foi o resultado do teste?'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='test',
            field=models.CharField(choices=[('RT-PCR', 'RT-PCR'), ('Sorologia', 'Sorologia'), ('Teste Rápido Antígenos', 'Teste Rápido Antígenos'), ('Teste Rápido Anticorpos', 'Teste Rápido Anticorpos')], max_length=40, verbose_name='Tipo de teste'),
        ),
    ]
