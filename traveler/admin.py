from django.contrib import admin
from .models import Team, Country, City, Address, Hotels, Gallery, Places, Travels, AboutUs, TravelCategory, PlaceCategories
# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_date', 'last_update')
    list_display_links = ('id', 'status')
    search_fields = ('id', 'status', 'about_us')
    list_filter = ('id', 'status')
    ordering = ('id',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'country__name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'price', 'discount', 'created_date')
    list_display_links = ('id', 'name', 'rating', 'price', 'discount', 'created_date')
    search_fields = ('id', 'name', 'rating', 'price', 'discount', )
    list_filter = ('id', 'name')
    ordering = ('id', 'name')


@admin.register(PlaceCategories)
class PlaceCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'last_updated')
    list_display_links = ('id', 'title', 'created_date', 'last_updated')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title')
    ordering = ('id', 'title')


@admin.register(TravelCategory)
class TravelCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name')
    ordering = ('id', 'name')


@admin.register(Travels)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'persons', 'price', 'price_type', 'discounts', 'departure_date', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'persons', 'price', 'price_type', 'discounts', 'departure_date', 'created_date', 'last_updated')
    search_fields = ('id', 'name', 'persons', 'price', 'discounts', 'departure_date')
    list_filter = ('id', 'name', 'persons', 'price')
    ordering = ('id', 'name')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'texts')
    list_display_links = ('id', 'name', 'texts')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = (('id', 'name'))

    def texts(self, obj):
        return obj.text[:10]
