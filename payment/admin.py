from django.contrib import admin
from .models import *
admin.site.register(Invoice)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('created_by','balance')
    search_fields = ('created_by',)
    list_editable = ('balance',)
    

admin.site.register(Balance, BalanceAdmin)
