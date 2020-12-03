from django.contrib import admin
from.models import Account, Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("author","title", "posted")

admin.site.register(Account)

admin.site.register(Blog, BlogAdmin)