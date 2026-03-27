
from django.contrib import admin
from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:id>/', detail, name='post_detail'),
]