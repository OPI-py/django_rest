from django.contrib import admin
from snippets.models import Snippet

# admin.site.register(Snippet)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
	list_display = ("title", "owner")
