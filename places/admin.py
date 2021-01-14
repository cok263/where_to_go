from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


MAX_PREVIEW_HEIGHT = 200

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = [
        'image', 
        'get_preview',
        'id',
    ]
    readonly_fields = [
        'get_preview',
    ]

    def get_preview(self, obj):
        if obj.image is None:
            return 'Изображение отсутствует'

        width = img.width
        height = img.height

        scale = height / MAX_PREVIEW_HEIGHT
        if scale > 1:
            height = MAX_PREVIEW_HEIGHT
            width = int(width / scale)

        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.image.url,
                width=width,
                height=height,
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
