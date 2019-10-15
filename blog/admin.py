from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)