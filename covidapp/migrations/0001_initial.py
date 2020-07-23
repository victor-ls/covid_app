# Generated by Django 3.0.8 on 2020-07-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('dateOfBirth', models.DateField(verbose_name='Data de nascimento')),
                ('test', models.CharField(max_length=40, verbose_name='Tipo de teste')),
                ('result', models.BooleanField(default=False, verbose_name='Resultado do teste')),
            ],
        ),
    ]
