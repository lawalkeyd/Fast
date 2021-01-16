from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Userss, ClientProfile


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'is_noob', 'is_elite', 'is_superuser')
    list_filter = ('is_noob', 'is_elite', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_noob', 'is_superuser', 'is_elite')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


class ClientProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Userss, UserAdmin)
admin.site.register(ClientProfile, ClientProfileAdmin)