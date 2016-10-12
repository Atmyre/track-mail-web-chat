from django.contrib import admin
from .models import *

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
# Register your models here.
