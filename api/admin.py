from django.contrib import admin

# Register your models here.
from api.models import Comment, Post, Group, Follow

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Follow)
