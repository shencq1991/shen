from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_time']

admin.site.register(Post, PostAdmin)
