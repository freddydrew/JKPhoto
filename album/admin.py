from django.contrib import admin
from .models import album, albumImage

# Register your models here.
class albumImageInline(admin.StackedInline):
    model = albumImage
    extra = 0

class albumAdmin(admin.ModelAdmin):
    # What fields I will see in the multiple objects view
    list_display = ['title','publish','publishDate']
    # For the uneditable fields
    readonly_fields = ['timeCreated','updated','slug']
    # The images that will appear beneath each album in the admin
    inlines = [albumImageInline]

admin.site.register(album,albumAdmin)
