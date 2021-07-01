from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogOption(admin.ModelAdmin):
    list_display = ('id', 'user', "title")
    search_fields = ('id',)
    save_on_top = True


admin.site.register(Blog, BlogOption)