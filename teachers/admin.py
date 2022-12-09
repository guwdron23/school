from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Teachers

class TeachersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'geo', 'phone',]

    # def image(obj):
    #     return mark_safe(f"<img src = {obj.image.url} wight = '100 height = '100'>")


admin.site.register(Teachers, TeachersAdmin)