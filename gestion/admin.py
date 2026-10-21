from django.contrib import admin
from .models import Proyecto, Tarea


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "fecha_creacion")
    search_fields = ("nombre",)


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "proyecto")
    list_filter = ("proyecto",)
    search_fields = ("titulo",)
