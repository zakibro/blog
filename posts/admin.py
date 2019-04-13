from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active')
    list_filter = ('active', 'author')
    date_hierarchy = 'pub_date'
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)
admin.site.site_header = u'Broski'

