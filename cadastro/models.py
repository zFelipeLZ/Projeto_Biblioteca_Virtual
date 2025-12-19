from django.db import models

class Livro(models.Model):
    STATUS_CHOICES = [
        ('D', 'Disponível'),
        ('L', 'Locado'),
    ]

    titulo = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')
    autor = models.CharField(max_length=150)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Locacao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_locacao = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
