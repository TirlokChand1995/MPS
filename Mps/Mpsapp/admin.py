from django.contrib import admin

# Register your models here.

from Mpsapp.models import Teachers, Gallery_main, Gallery

admin.site.register(Teachers)
admin.site.register(Gallery)
admin.site.register(Gallery_main)