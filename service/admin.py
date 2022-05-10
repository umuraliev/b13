from django.contrib import admin
from .models import *


admin.site.register(Barber)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Category, CategoryAdmin)

class EntriesTimeAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'time']

admin.site.register(EntriesTime, EntriesTimeAdmin)