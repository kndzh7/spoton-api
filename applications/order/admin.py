from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Order, OrderAdmin)
