from django.contrib import admin
from .models import *

@admin.register(Chat)
class Chatdmin(admin.ModelAdmin):
    pass
# Register your models here.
