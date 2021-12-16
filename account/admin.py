from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Interesting, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Interesting)
class InterestingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Custom fiels'), {'fields': ('image', 'birthday', 'interestings')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'is_staff', 'birthday')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'telefon')
    ordering = ('id',)
