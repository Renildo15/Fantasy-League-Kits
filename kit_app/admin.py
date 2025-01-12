from django.contrib import admin
from django.utils.html import format_html

from .models import Kit

# Register your models here.


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = (
        "club",
        "kit_home_preview",
        "kit_away_preview",
        "kit_goalkeeper_home_preview",
        "kit_goalkeeper_away_preview",
        "kit_version",
        "kit_current",
        "kit_type",
        "created_at",
        "updated_at",
    )
    list_filter = ("club", "kit_current", "kit_type", "created_at", "updated_at")
    search_fields = ("club", "kit_version")
    readonly_fields = (
        "kit_home_preview",
        "kit_away_preview",
        "created_at",
        "updated_at",
    )

    def kit_home_preview(self, obj):
        if obj.kit_home:
            return format_html(
                '<a href={}><img src="{}" style="height: 50px;"/></a>',
                obj.kit_home_url or obj.kit_home.url,
                obj.kit_home_url or obj.kit_home.url,
            )
        return "No Home Kit"

    kit_home_preview.short_description = "Home Kit"

    def kit_away_preview(self, obj):
        if obj.kit_away:
            return format_html(
                '<a href={}><img src="{}" style="height: 50px;"/></a>',
                obj.kit_away_url or obj.kit_away.url,
                obj.kit_away_url or obj.kit_away.url,
            )
        return "No Away Kit"

    kit_away_preview.short_description = "Away Kit"

    def kit_goalkeeper_home_preview(self, obj):
        if obj.kit_goalkeeper_home:
            return format_html(
                '<a href={}><img src="{}" style="height: 50px;"/></a>',
                obj.kit_goalkeeper_home_url or obj.kit_goalkeeper_home.url,
                obj.kit_goalkeeper_home_url or obj.kit_goalkeeper_home.url,
            )
        return "No Home Goalkeeper Kit"

    def kit_goalkeeper_away_preview(self, obj):
        if obj.kit_goalkeeper_away:
            return format_html(
                '<a href={}><img src="{}" style="height: 50px;"/></a>',
                obj.kit_goalkeeper_away_url or obj.kit_goalkeeper_away.url,
                obj.kit_goalkeeper_away_url or obj.kit_goalkeeper_away.url,
            )
        return "No Away Goalkeeper Kit"
