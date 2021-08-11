from django.db import models

# Create your models here.

class ExitTicket(models.Model):
    OCUPACOES = (
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('EST', 'Estudante')
    )

    DUVIDAS = (
        ('PY', 'Python'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS')
    )

    nome = models.CharField(max_length=200)
    email = models.EmailField()
    ocupacao = models.CharField(max_length=3, choices=OCUPACOES)
    feedback = models.TextField()
    data = models.DateField()
    nota = models.PositiveIntegerField(default=0)
    duvidas = models.CharField(max_length=4, choices=DUVIDAS)

    data_publicacao = models.DateTimeField(auto_now_add=True)
