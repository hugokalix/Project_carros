from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #São os campos que quero que apareça para meu usuario
    search_fields = ('model', )


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)





