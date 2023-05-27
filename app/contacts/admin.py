from django.contrib import admin

from .models import *


class NumberInline(admin.StackedInline):
    model = Number

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    inlines = [NumberInline]
