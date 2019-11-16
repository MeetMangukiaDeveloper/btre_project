from django.contrib import admin

# Register your models here.

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'discription', 'address', 'city', 'state', 'zipcode',
    'price')

admin.site.register(Listing, ListingAdmin)