from django.contrib.admin import register, ModelAdmin
from ..models import Products


@register(Products)
class Products(ModelAdmin):
    list_display = ("name", "price", "description")
    list_display_links = ("name", "price",)
    search_fields = ("name", "price", "description")

