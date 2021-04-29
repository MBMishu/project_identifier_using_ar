from django.contrib import admin
from home.model.models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','phone','email')
    search_fields = ['user','name','phone','email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','customer','markerURL','productModelURL')
    search_fields = ['name','customer']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)