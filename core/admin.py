from django.contrib import admin
from .models import Contacto, Project

# Register your models here.

admin.site.register(Contacto)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project,ProjectAdmin)