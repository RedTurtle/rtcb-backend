# -*- coding: utf-8 -*-
from .authentication.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rtcb.team.models import Team
from rtcb.tournament.models import Tournament
from rtcb.match.models import Match
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)


admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """ Preso direttamente da django.
    django/contrib/auth/admin.py
    django/contrib/auth/forms.py
    """
    add_form_template = 'admin/auth/user/add_form.html'
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
