# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    class meta:
        model = Post

admin.site.register(Post,PostModelAdmin)