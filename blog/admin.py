from django.contrib import admin
from .models import Category, Post, Comment

# Configuración opcional para ver más detalles de los posts en el panel
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'category')
    list_filter = ('status', 'created_at', 'category')
    search_fields = ('title', 'body')

# Configuración para ver los comentarios de forma ordenada
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'body', 'email')

# Registro de los modelos
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)