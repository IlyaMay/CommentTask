from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment, MPTTModelAdmin)
