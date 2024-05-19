from rest_framework import serializers
from django.contrib.auth.models import User
from traveler.models import (Country, City, Address, Team, Gallery, Hotels, PlaceCategories, Places, TravelCategory,
        Comments, Travels, AboutUs, BookNow)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'created_date']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'number_views', 'image', 'created_date']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name', 'city', 'created_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class TeamSerializer(serializers.ModelSerializer):
    employee = UserSerializer()

    class Meta:
        model = Team
        fields = ['id', 'employee', 'status', 'image', 'created_date']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'name', 'image', 'looking_numbers', 'created_date', 'last_updated']


class HotelsSerializer(serializers.ModelSerializer):
    images = GallerySerializer(many=True)

    class Meta:
        model = Hotels
        fields = ['id', 'name', 'rating', 'images', 'brand_image', 'price', 'price_type', 'service_term', 'discount', 'created_date']


class PlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategories
        fields = ['id', 'name', 'looking_count', 'created_date']


class PlacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Places
        fields = ['id', 'author', 'title', 'address', 'hotels', 'category', 'created_date']


class TravelCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelCategory
        fields = ['id', 'author', 'name', 'image', 'created_date']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comments
        fields = ['id', 'user', 'text', 'reads_number', 'created_date']


class TravelSerializer(serializers.ModelSerializer):
    author = TeamSerializer()

    class Meta:
        model = Travels
        fields = ['id', 'author', 'name', 'persons', 'price', 'price_type', 'description', 'image', 'category', 'comments', 'likes', 'places', 'discounts', 'departure_date', 'return_day', 'created_date']


class AboutUsSerializer(serializers.ModelSerializer):
    hotels = HotelsSerializer(many=True)
    travels = TravelSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ['id', 'name', 'text', 'hotels', 'travels', 'created_date']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookNow
        fields = ['id', 'full_name', 'email', 'persons', 'users', 'travel', 'created_date']


