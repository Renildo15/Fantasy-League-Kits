from django.contrib import admin
from django.utils.html import format_html

from .models import Club

# Register your models here.


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "emblem_preview",
        "clickable_emblem_url",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("emblem_preview", "created_at", "updated_at")

    def emblem_preview(self, obj):
        if obj.emblem:
            return format_html(
                '<img src="{}" style="height: 50px;"/>',
                obj.emblem_url or obj.emblem.url,
            )
        return "No Emblem"

    emblem_preview.short_description = "Emblem"

    def clickable_emblem_url(self, obj):
        if obj.emblem_url:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', obj.emblem_url, obj.emblem_url
            )
