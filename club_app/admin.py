from django.contrib import admin
from django.utils.html import format_html

from .models import Club

# Register your models here.


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "emblem_preview",
        "clickable_emblem_url_512",
        "clickable_emblem_url_original",
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
                obj.emblem_versions.get("512x512")
                or obj.emblem_versions.get("512x512"),
            )
        return "No Emblem"

    emblem_preview.short_description = "Emblem"

    def clickable_emblem_url_512(self, obj):
        if obj.emblem_versions:
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                obj.emblem_versions.get("512x512"),
                obj.emblem_versions.get("512x512"),
            )
        return "No Emblem"

    clickable_emblem_url_512.short_description = "Emblem URL (512x512)"

    def clickable_emblem_url_original(self, obj):
        if obj.emblem_versions:
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                obj.emblem_versions.get("original"),
                obj.emblem_versions.get("original"),
            )
        return "No Emblem"

    clickable_emblem_url_original.short_description = "Emblem URL (Original)"
