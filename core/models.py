from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Informe 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    """
    ForeignKey ==> Cada Montadora possui muitos Carros mas cada Carro
    possui apenas 1 montadora
    """
    nome = models.CharField('Nome', max_length=50, help_text='Tamanho máximo de 20 caracteres')

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


class Carro(models.Model):
    """
    OneToOneField ==> Cada Carro possui 1 Chassi e cada Chassi
    estará presente em apenas 1 Carro
    ManyToManyField ==> 1 Carro pode ser dirigido por vários Motoristas e 1 Motorista pode dirigir muitos Carros
    """
    montadora = models.ForeignKey('Montadora', on_delete=models.CASCADE)
    chassi = models.OneToOneField('Chassi', on_delete=models.CASCADE)  # Utilizando a relacao 1 pra 1
    modelo = models.CharField('Modelo', max_length=30, help_text='Tamanho máximo de 30 caracteres')
    motorista = models.ManyToManyField(get_user_model())
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'


