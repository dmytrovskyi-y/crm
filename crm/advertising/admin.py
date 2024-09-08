from django.contrib import admin
from .models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Base options", {
                "fields": ["name", "promotion", "budget", "service", "date"],

            }
        ),
    ]
    list_display = ["pk", "name", "budget", "date"]
    list_display_links = ["name"]
    list_editable = ["budget"]
    list_per_page = 20
    list_filter = ["date"]
    readonly_fields = ["date"]
    ordering = ["pk", "date", "budget"]
    search_fields = ["name"]
    search_help_text = "Search in ads names"
    filter_horizontal = ["service"]
