from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'color', 'price', 'owner', 'created_at']
    list_filter = ['brand', 'year', 'color', 'created_at']
    search_fields = ['brand', 'model', 'color']
    list_per_page = 20
    ordering = ['-created_at']
