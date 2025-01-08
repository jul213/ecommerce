from django.contrib import admin
from  .models import product

class productoAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "precio")
    search_fields = ("name", "precio")
    list_filter = ("name",)
    #date_herarchi = "date" esto es para fechas filtrado especifico



admin.site.register(product, productoAdmin)