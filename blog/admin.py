from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title" , "author", "date"]
    list_filter = ["author", "date", "tag"]
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post" , "user_name" , "text"]
    list_filter  = ["id"]
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment , CommentAdmin)