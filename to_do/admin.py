from django.contrib import admin

from to_do.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_editable = ['status']
