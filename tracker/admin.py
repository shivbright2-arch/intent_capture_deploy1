from django.contrib import admin
from .models import IntentVisitor

# Register your models here.
#admin.site.register(IntentVisitor)

@admin.register(IntentVisitor)
class IntentVisitorAdmin(admin.ModelAdmin):
    list_display = (
        'session_id',
        'keyword',
        'source',
        'intent_level',
        'flipkart_clicked',
        'ip_address',
        'created_at',
    )
