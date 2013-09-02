from django.contrib import admin
from models import *

class CalendarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')
    search_fields = ['title']
    date_hierarchy = 'start'

admin.site.register(Event, EventAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(msg)
