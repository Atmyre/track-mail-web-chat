from django.contrib import admin
from .models import *

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass
# Register your models here.
