from django.contrib import admin
from contact.models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'subject', 'message', 'created_date', 'updated_date']
    search_fields = ['name', 'email', 'subject', 'message', ]

    class Meta:
        model = Message
