# -*- coding: utf-8 -*-
from django.db import models

# 1. Categorías para organizar tus posts
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    # Nuevo campo para el color (puedes poner 'yellow', 'blue', o códigos HEX)
    color_hex = models.CharField(max_length=7, default='#FFC107') 

    def __str__(self):
        return self.title

# 2. El Post principal (Álbumes, reseñas, etc.)
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) # Importante para las URLs
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

# 3. ESPECIFICACIONES DINÁMICAS (Lo que pediste)
# Sirve para agregar "Artista: Pepe Madero", "Género: Rock", etc.
class Specification(models.Model):
    post = models.ForeignKey(Post, related_name='specs', on_delete=models.CASCADE)
    label = models.CharField(max_length=50) # Ejemplo: "Artista"
    value = models.CharField(max_length=255) # Ejemplo: "José Madero"

    def __str__(self):
        return f"{self.label}: {self.value}"

# 4. Sistema de Comentarios
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.name} en {self.post.title}"