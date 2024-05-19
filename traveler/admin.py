from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Team, Country, City, Address, Hotels, Gallery, Places, Travels, AboutUs, TravelCategory, PlaceCategories, Comments, BookNow
# Register your models here.


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'status', 'created_date', 'last_update')
    prepopulated_fields = {"slug": ("status",)}
    list_display_links = ('id', 'status')
    search_fields = ('id', 'status', 'about_us')
    list_filter = ('id', 'status')
    ordering = ('id',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'country__name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Gallery)
class GalleryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id',)


@admin.register(Hotels)
class HotelsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'rating', 'price', 'discount', 'created_date')
    prepopulated_fields = {"slug": ("name",)}
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
class PlacesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'created_date', 'last_updated')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title', 'created_date', 'last_updated')
    search_fields = ('id', 'title')
    list_filter = ('id', 'title')
    ordering = ('id', 'title')


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'texts', 'created_date', 'last_updated')
    list_display_links = ('id', 'texts', 'created_date', 'last_updated')
    search_fields = ('id', 'texts')
    list_filter = ('id', )
    ordering = ('id', 'created_date')

    def texts(self, obj):
        return obj.text[:10]

@admin.register(TravelCategory)
class TravelCategoriesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date', 'last_updated')
    list_display_links = ('id', 'name', 'created_date', 'last_updated')
    search_fields = ('id', 'name',)
    list_filter = ('id', 'name')
    ordering = ('id', 'name')


@admin.register(Travels)
class TravelAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'persons', 'price', 'price_type', 'discounts', 'departure_date', 'created_date', 'last_updated')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id', 'name', 'persons', 'price', 'price_type', 'discounts', 'departure_date', 'created_date', 'last_updated')
    search_fields = ('id', 'name', 'persons', 'price', 'discounts', 'departure_date')
    list_filter = ('id', 'name', 'persons', 'price')
    ordering = ('id', 'name')


@admin.register(AboutUs)
class AboutUsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'texts')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id', 'name', 'texts')
    search_fields = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id', )

    def texts(self, obj):
        return obj.text[:10]


@admin.register(BookNow)
class BookNowAdmin(ImportExportModelAdmin):
    list_display = ('id', 'full_name', 'email', 'persons', 'created_date', 'last_updated')
    list_display_links = ('id', 'full_name', 'email', 'persons', 'created_date', 'last_updated')
    search_fields = ('id', 'full_name', 'email')
    list_filter = ('id', 'full_name', 'email')
    ordering = ('id', )
