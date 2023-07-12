from django.contrib import admin
from .models import Genre, Category, Theme, Movies

admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(Movies)