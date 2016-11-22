from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'timestamp')
    list_display_links = ('updated',)
    list_filter = ('updated', 'timestamp')
    list_editable = ('title',)
    # readonly_fields = ('updated', 'timestamp')

    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
