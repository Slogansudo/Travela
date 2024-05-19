from django.urls import path
from .views import (AboutUsView, ServicesView, BlogsView, HotelsView, HotelDetailView, HotelBookingView, ExploreTravelView, TravelPlacesView, PlacesView, CityPlacesView, BookNowView,
                   BookingDetailView, DeleteBookedView)

urlpatterns = [
    path('about/', AboutUsView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('hotels/', HotelsView.as_view(), name='hotels'),
    path('hotels/<slug:slug>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('hotels/<slug:slug>/booking/', HotelBookingView.as_view(), name='hotel_booking'),
    path('places/<slug:slug>/', PlacesView.as_view(), name='places'),
    path('explore-travel/', ExploreTravelView.as_view(), name='explore_tour'),
    path('city-places/<int:id>/', CityPlacesView.as_view(), name='city_places'),
    path('viewplaces/<slug:slug>/', TravelPlacesView.as_view(), name='viewplaces'),
    path('booknow/<slug:slug>/', BookNowView.as_view(), name='booknow'),
    path('booknow/detail', BookingDetailView.as_view(), name='booking_detail'),
    path('deletebook/<int:id>/', DeleteBookedView.as_view(), name='booked_delete')

]
