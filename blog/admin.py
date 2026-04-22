from django.contrib import admin
from .models import Category, Post, Comment, Specification

# 1. Esta clase define CÓMO se verán las specs dentro del post
class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 2  # Esto te pondrá 2 filas vacías para llenar de inmediato

# 2. Esta clase le dice al Post que incluya las specs
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    # ESTA LÍNEA ES LA QUE FALTA EN TU IMAGEN:
    inlines = [SpecificationInline] 
    prepopulated_fields = {'slug': ('title',)}

# 3. Registros (Asegúrate de no tener registros repetidos abajo)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)