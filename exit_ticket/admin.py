from django.contrib import admin
from exit_ticket.models import ExitTicket

# Register your models here.

class ExitTicketAdmin(admin.ModelAdmin):
    list_filter = ['nome']
    list_display = ['nome', 'data', 'nota']

admin.site.register(ExitTicket, ExitTicketAdmin)
