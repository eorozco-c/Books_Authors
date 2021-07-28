from django.db import models

# Create your models here.
class Libro(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Autor(models.Model):
    libros = models.ManyToManyField(Libro, related_name='autores')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notas = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)