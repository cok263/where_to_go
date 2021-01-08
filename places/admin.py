from django.contrib import admin
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = [
        'image', 
        'id', 
        #'place',
    ]
    #can_delete = False
    #raw_id_fields = ("id",)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
