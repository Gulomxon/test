from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accaunt, SubProfession, Profession, Contact
from django.contrib.auth.models import Group

class AccauntAdmin(UserAdmin):
    list_display        = ('username', Accaunt.get_full_name, 'data_joined', 'last_login')
    search_fields       = ('username',)
    readonly_fields     = ('data_joined', 'last_login', 'borth_day')

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()

admin.site.register(Accaunt, AccauntAdmin)
admin.site.unregister(Group)

admin.site.register(SubProfession)
admin.site.register(Profession)
admin.site.register(Contact)