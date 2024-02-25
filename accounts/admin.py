from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from accounts.forms import UserChangeForm, UserCreationForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = [
        "email",
        "username",
        "is_admin",
        "is_superuser",
    ]
    list_filter =[]
    
    fieldsets = [
        (None,  {"fields": ("email",)}),
        ("Personal Information", {"fields": ("username", )}),
        ("Credentials", {"fields": ("password", "password2", )}),
        ("permissions", {"fields": ("is_admin", "is_superuser")}),
    ]
    
    add_fieldsets = [
        (None, {"classes": ['wide'], "fields": ('username', 'email', 'password', 'password2')}),
    ]
    
    search_fields = ['email']
admin.site.register(User, UserAdmin)
