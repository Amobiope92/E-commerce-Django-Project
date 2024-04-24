from django.contrib import admin

from . models import profile, product
# Register your models here.

# admin.site.register(profile)
admin.site.register(product)

@admin.register(profile) #we use this whenever we want to make use of specific columns, in this case 'user, position & state'
class profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'state', ]
