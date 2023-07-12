from django.contrib import admin
from .models import *
# Register your models here.

class PostImageInLine(admin.TabularInline):
    model = PostImage
    max_num =10
    min_num =1

@admin.register(Movies)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine, ]


admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Theme)
# admin.site.register(Movies)