
from django.contrib import admin
from .models import product,category

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','update','created']
    list_editable = ['price','available','slug']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}

admin.site.register(product,productadmin)
