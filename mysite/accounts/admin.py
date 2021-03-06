from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GeneralUser

# Register your models here.

admin.site.register(GeneralUser, UserAdmin)
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('user_type', 'is_activated', ),}),