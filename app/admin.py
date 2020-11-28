from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','info','user')
    list_editable = ('info',) 
    list_per_page = 10
    search_fields = ('name','email','phone','info','user')
    list_filter = ('user', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)