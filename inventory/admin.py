from django.contrib import admin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image_tag', 'created_at')  # show image
    search_fields = ('name', 'description')
    list_filter = ('stock',)

    readonly_fields = ('created_at', 'updated_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
