from django.contrib import admin

# Register your models here.
from .models import User

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_admin", "is_active")