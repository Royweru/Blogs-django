from django.contrib import admin
from .models import Topic,Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'title', 'body', 'updated', 'created')

admin.site.register(Topic)
admin.site.register(Post,PostAdmin)