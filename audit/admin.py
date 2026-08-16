from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "action",
        "document",
        "ip_address",
        "created_at",
    )

    list_filter = (
        "action",
        "created_at",
    )

    search_fields = (
        "user__email",
        "document__title",
        "description",
    )

    readonly_fields = (
        "user",
        "action",
        "document",
        "description",
        "ip_address",
        "created_at",
    )