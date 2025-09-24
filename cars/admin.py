from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'color', 'price', 'owner', 'created_at']
    list_filter = ['brand', 'year', 'color', 'created_at', 'owner']
    search_fields = ['brand', 'model', 'color', 'owner__username']
    list_per_page = 20
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informasi Mobil', {
            'fields': ('brand', 'model', 'year', 'color', 'price')
        }),
        ('Kepemilikan', {
            'fields': ('owner',)
        }),
        ('Timestamp', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Jika objek baru
            obj.owner = request.user
        super().save_model(request, obj, form, change)

# Extend User admin to show permissions
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_active', 'date_joined')
    list_filter = UserAdmin.list_filter + ('groups',)
    
    # Override fieldsets to avoid duplicate fields
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Re-register User with custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
