from django.contrib import admin
from .models import Post_data,Categories,Comment
# Register your models here.
admin.site.register(Post_data)
admin.site.register(Categories)
admin.site.register(Comment)