from django.contrib import admin
from blog import models
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
admin.site.register(models.BlogPost, BlogPostAdmin)

class PrivateBlogAdmin(admin.ModelAdmin):
    list_display = ('title','username','timestamp')
admin.site.register(models.PrivateBlog, PrivateBlogAdmin)
# Register your models here.
