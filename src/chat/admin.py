from django.contrib import admin
from .models import *


class MembershipInline(admin.TabularInline):
    model = Membership
    fk_name = 'chat'


class ChatAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)


admin.site.register(Chat, ChatAdmin)