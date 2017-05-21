from django.contrib import admin
from .models import Post

#Register the model
admin.site.register(Post)#make model visible on admin page
