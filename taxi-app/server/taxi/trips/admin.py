from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
	pass