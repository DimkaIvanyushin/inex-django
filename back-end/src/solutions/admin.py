from django.contrib import admin

from .models import Solutions, Comment
    
class SolutionsCommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class SolutionsAdmin(admin.ModelAdmin):
    inlines = [ SolutionsCommentInline ]

admin.site.register(Solutions, SolutionsAdmin)