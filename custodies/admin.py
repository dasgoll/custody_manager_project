from django.contrib import admin

from .models import Custody


class CustodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'description', 'serial_number',
                    'created_at')
    list_display_links = ('id', 'description')
    list_filter = ('employee', )
    list_per_page = 25


admin.site.register(Custody, CustodyAdmin)
