from django.contrib import admin
from django.utils.html import format_html

from .models import Championship

# Register your models here.


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "logo_preview",
        "clickable_logo_url_512",
        "clickable_logo_url",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("logo_preview", "created_at", "updated_at")

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height: 50px;"/>', obj.logo_versions.get("512x512") or obj.logo_versions.get("512x512")
            )
        return "No Logo"

    logo_preview.short_description = "Logo"

    def clickable_logo_url_512(self, obj):
        if obj.logo_versions:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', obj.logo_versions.get("512x512"), obj.logo_versions.get("512x512")
            )
        return "No URL"

    clickable_logo_url_512.short_description = "Logo URL (512x512)"

    def clickable_logo_url(self, obj):
        if obj.logo_versions:
            return format_html(
                '<a href="{}" target="_blank">{}</a>', obj.logo_versions.get("original"), obj.logo_versions.get("original")
            )
        return "No URL"
    
    clickable_logo_url.short_description = "Logo URL (Original)"