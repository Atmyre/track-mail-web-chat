from django.contrib import admin
from .models import *

@admin.register(Community)
class CommuniryAdmin(admin.ModelAdmin):
    pass
# Register your models here.
