from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class New(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    texto = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,
                              blank=True, null=True, related_name='autor_news')

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    ativado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['-criado']

    def __str__(self):
        return f'Comentário de: {self.usuario.get_full_name()}'