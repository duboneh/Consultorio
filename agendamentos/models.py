from operator import mod
from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField('Nome do paciente', max_length=250)
    cpf = models.CharField('CPF ', max_length=14, help_text="Digite somente os números.")
    email = models.CharField('E-mail', max_length=250, null=True, blank=True)
    data_nascimento = models.DateField('Data de Nascimento', help_text="DD/MM/AAAA")
    celular = models.CharField('Núm. celular', max_length=250, help_text="Digite somente os números.")
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Agendamento(models.Model):
    TIPO_CHOICES = [
                (1, 'Urgência'),
                (2, 'Avaliação'),
                (3, 'Paciente em tratamento'),
                (4, 'Retorno'),
                (5, 'Parceria'),
            ]
    
    ESP_CHOICES = [
                (1, 'Cirurgia'),
                (2, 'Endodontia'),
                (3, 'Ortodontia'),
                (4, 'HOF'),
                (5, 'Protese'),
                (6, 'Implantodontia'),
            ]
    
    PAGAMENTO_CHOICES = [
                (1, 'Particular'),
                (2, 'Plano de Saúde'),
                (3, 'Parceria'),
            ]
    
    HORARIO_CHOICES = [
                (8, 8),
                (9, 9),
                (10, 10),
                (11, 11),
                (12, 12),              
                (14, 14),
                (15, 15),
                (16, 16),
                (17, 17),
                (18, 18),
            ]
        
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    #nome = models.CharField('Nome do paciente', max_length=250)#
    #cpf = models.CharField('CPF ', max_length=14, help_text="Digite somente os números.")#
    tipo_consulta = models.IntegerField(verbose_name='Tipo de Consulta', choices=TIPO_CHOICES)
    #email = models.CharField('E-mail', max_length=250, null=True, blank=True)#
    #data_nascimento = models.DateField('Data de Nascimento', help_text="DD/MM/AAAA")#
    #celular = models.CharField('Núm. celular', max_length=250)#
    pagamento = models.IntegerField('Pagamento', choices=PAGAMENTO_CHOICES)  
    especialidade = models.IntegerField('Especialidade', choices=ESP_CHOICES)
    data_consulta = models.DateField('Data consulta', help_text="DD/MM/AAAA")
    hora_consulta = models.IntegerField('Horário consulta', choices=HORARIO_CHOICES)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    
    def __str__(self):
        return str(self.paciente)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas agendadas'


