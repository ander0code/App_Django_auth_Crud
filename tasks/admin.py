from django.contrib import admin
from .models import Task

#para hacer que las columnas sean de solo lectura
class TaskAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created",)
    
    
# Register your models here.
admin.site.register(Task,TaskAdmin)