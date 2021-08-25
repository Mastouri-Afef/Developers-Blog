from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import DomainUserChangeForm


class DomainUserAdmin(UserAdmin):
    form = DomainUserChangeForm


admin.site.unregister(User)
admin.site.register(User, DomainUserAdmin)
admin.site.register(Profile)
