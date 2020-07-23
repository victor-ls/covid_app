from django.db import models


class Patient(models.Model):
    fullName = models.CharField('Nome completo', max_length=100)
    dateOfBirth = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False)
    testOptions = [
        ('RT-PCR', 'RT-PCR'),
        ('Sorologia', 'Sorologia'),
        ('Teste Rápido Antígenos', 'Teste Rápido Antígenos'),
        ('Teste Rápido Anticorpos', 'Teste Rápido Anticorpos')
    ]
    test = models.CharField('Tipo de teste', max_length=40, choices=testOptions)
    resultOptions = [
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo')
    ]
    result = models.CharField('Qual foi o resultado do teste?', max_length=20, choices=resultOptions)

    def __str__(self):
        return self.fullName
