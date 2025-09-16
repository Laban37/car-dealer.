from django.contrib import admin
from django.utils.html import format_html
from .models import Car, CarImage


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:5px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'transmission', 'main_image_preview', 'image_count')
    search_fields = ('brand', 'model')
    list_filter = ('brand', 'year', 'transmission')
    inlines = [CarImageInline]

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="100" style="border-radius:5px;"/>', obj.main_image.url)
        return "-"
    main_image_preview.short_description = "Main Image"

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = "Gallery Images"
