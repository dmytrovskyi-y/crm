from django.contrib import admin, messages

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Base options", {
                "fields": ["description", "name", "is_active", "price"],

            }
        ),
    ]
    actions = ["set_active", "set_not_active"]
    list_display = ["name", "is_active", "price", "pk"]
    list_filter = ["is_active"]
    list_per_page = 20
    ordering = ["name", "price", "is_active"]
    save_as = True
    search_fields = ["name"]
    search_help_text = "Search in product names"

    @admin.action(description="Activate the service")
    def set_active(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f"Services activated: {count}")

    @admin.action(description="Deactivate the service")
    def set_not_active(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(request, f"Services deactivated: {count}", messages.WARNING)
