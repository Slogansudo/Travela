from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import User
from django.db.transaction import atomic
from rest_framework.decorators import action
from datetime import datetime
from traveler.models import (Country, City, Address, Team, Gallery, Hotels, PlaceCategories, Places, TravelCategory,
        Comments, Travels, AboutUs, BookNow)
from .serializer import (CommentSerializer, CountrySerializer, CitySerializer, AddressSerializer, UserSerializer,
            TeamSerializer, GallerySerializer, HotelsSerializer, PlaceCategorySerializer, PlacesSerializer, TravelCategorySerializer,
            TravelSerializer, AboutUsSerializer, BookingSerializer)


class CountryAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated, ]
    #authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order_id(self, request, *args, **kwargs):
        countries = self.get_queryset()
        countries = countries.order_by('-id')
        serializer = CountrySerializer(countries, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CityAPIViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'country__name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order_id(self, request, *args, **kwargs):
        city = self.get_queryset()
        city = city.order_by('-id')
        serializer = CitySerializer(city, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def famous_city(self, request, *args, **kwargs):
        city = self.get_queryset()
        city = city.order_by('-number_views')[:4]
        serializer = CitySerializer(city, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def country(self, request, *args, **kwargs):
        city = self.get_object()
        country = city.country
        serializer = CountrySerializer(country)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def looking_for_city(self, request, *args, **kwargs):
        city = self.get_object()
        with atomic():
            city.number_views += 1
            city.save()
            serializer = CitySerializer(city)
            return Response(serializer.data, status=status.HTTP_200_OK)


class AddressAPIViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'city__name', 'city__country__name', 'city__created_date']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def new_addresses(self, request, *args, **kwargs):
        address = self.get_queryset()
        address = address.order_by('-created_date')[:5]
        serializer = AddressSerializer(address, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def city(self, request, *args, **kwargs):
        address = self.get_object()
        city = address.city
        serializer = CitySerializer(city)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def country(self, request, *args, **kwargs):
        address = self.get_object()
        country = address.city.country
        serializer = CountrySerializer(country)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TeamAPIViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminUser, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'employee__username', 'status', 'employee__first_name', 'employee__last_name']

    @action(detail=False, methods=['get'])
    def admins(self, request, *args, **kwargs):
        teams = self.get_queryset()
        data = []
        for team in teams:
            if team.employee.is_superuser == True:
                data.append(team)
        serializer = TeamSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def employee(self, request, *args, **kwargs):
        team = self.get_object()
        employee = team.employee
        serializer = UserSerializer(employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def managers(self, request, *args, **kwargs):
        team = self.get_queryset()
        team = team.filter(status__icontains='manager')
        serializer = TeamSerializer(team, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GalleryAPIViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'created_date']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        galleries = self.get_queryset()
        galleries = galleries.order_by('-id')
        serializer = GallerySerializer(galleries, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def new_photos(self, request, *args, **kwargs):
        galleries = self.get_queryset()
        galleries = galleries.order_by('-created_date')[:5]
        serializer = GallerySerializer(galleries, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def looking_photos(self, request, *args, **kwargs):
        gallery = self.get_object()
        with atomic():
            gallery.looking_numbers += 1
            gallery.save()
            return Response(status=status.HTTP_200_OK)


class HotelsAPIViewSet(ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [AllowAny, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'rating', 'price', 'price_type', 'service_term', 'discount']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def top_hotels(self, request, *args, **kwargs):
        hotels = self.get_queryset()
        hotels = hotels.order_by('-rating')[:3]
        serializer = HotelsSerializer(hotels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def discount_hotels(self, request, *args, **kwargs):
        hotels = self.get_queryset()
        hotels = hotels.order_by('-discount')
        serializer = HotelsSerializer(hotels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def images(self, request, *args, **kwargs):
        hotel = self.get_object()
        images = hotel.images.all()
        serializer = GallerySerializer(images, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PlaceCategoryAPIViewSet(ModelViewSet):
    queryset = PlaceCategories.objects.all()
    serializer_class = PlaceCategorySerializer
    permission_classes = [IsAuthenticated, ]
    #authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'created_date']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        placescategories = self.get_queryset()
        placescategories = placescategories.order_by('-id')
        serializer = PlaceCategorySerializer(placescategories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def looking(self, request, *args, **kwargs):
        category = self.get_object()
        with atomic():
            category.looking_count += 1
            category.save()
            serializer = PlaceCategorySerializer(category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def top_looking_count(self, request, *args, **kwargs):
        category = self.get_queryset()
        category = category.order_by('-looking_count')
        serializer = PlaceCategorySerializer(category, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PlacesAPIViewSet(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'author__status', 'author__employee__username', 'author__employee__first_name', 'author__employee__last_name','title', 'address__name',
                     'address__city__name', 'hotels__name', 'hotels__rating', 'hotels__discount', 'category__name', 'created_date']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['get'])
    def address(self, request, *args, **kwargs):
        place = self.get_object()
        address = place.address
        serializer = AddressSerializer(address)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def city(self, request, *args, **kwargs):
        place = self.get_object()
        city = place.address.city
        serializer = CitySerializer(city)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def hotels(self, request, *args, **kwargs):
        place = self.get_object()
        hotels = place.hotels.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def category(self, request, *args, **kwargs):
        place = self.get_object()
        categories = place.category
        serializer = PlaceCategorySerializer(categories)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def author(self, request, *args, **kwargs):
        place = self.get_object()
        author = place.author
        serializer = TeamSerializer(author)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TravelCategoryAPIViewSet(ModelViewSet):
    queryset = TravelCategory.objects.all()
    serializer_class = TravelCategorySerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'author__status', 'author__employee__username', 'author__employee__first_name', 'author__employee__last_name',
                     'name', 'created_date']

    @action(detail=True, methods=['get'])
    def author(self, request, *args, **kwargs):
        place = self.get_object()
        author = place.author
        serializer = TeamSerializer(author)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        places = self.get_queryset()
        places = places.order_by('-id')
        serializer = PlaceCategorySerializer(places, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def today_category(self, request, *args, **kwargs):
        places = self.get_queryset()
        places = places.filter(created_date__icontains=datetime.now().strftime('%Y-%m-%d'))
        serializer = PlaceCategorySerializer(places, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentAPIViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['text', 'id', 'user__username', 'user__first_name', 'user__last_name']
    pagination_classes = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def today_comments(self, request, *args, **kwargs):
        comments = self.get_queryset()
        comment1 = comments.filter(created_date__icontains=datetime.now().date())
        serializer = CommentSerializer(comment1, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def re_orders(self, request, *args, **kwargs):
        comments = self.get_queryset()
        orders = comments.order_by('-id')
        serializer = CommentSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def my_comments(self, request, *args, **kwargs):
        comments = self.get_queryset()
        comment1 = comments.filter(user=request.user)
        serializer = CommentSerializer(comment1, many=True)
        if comment1.count() > 0:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=[], status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def looking_for_comment(self, request, *args, **kwargs):
        comment = self.get_object()
        with atomic():
            comment.reads_number += 1
            comment.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def top_reads_comment(self, request, *args, **kwargs):
        comment = self.get_queryset()
        comment = comment.order_by('-reads_number')[:3]
        serializer = CommentSerializer(comment, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TravelAPIViewSet(ModelViewSet):
    queryset = Travels.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'author__status', 'author__employee__first_name', 'author__employee__last_name',
                     'name', 'persons', 'price', 'price_type', 'description', 'category__name', 'category__author__employee__first_name', 'category__author__employee__last_name',
                     'likes', 'places__title', 'places__author__employee__last_name', 'places__address__name', 'places__address__city__name',
                     'places__address__city__country__name', 'discounts', 'departure_date']
    pagination_classes = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def top_likes_travel(self, request, *args, **kwargs):
        travels = self.get_queryset()
        travels = travels.order_by('-likes')[:1]
        serializer = TravelSerializer(travels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def top_comments_travel(self, request, *args, **kwargs):
        travelss = self.get_queryset()
        travel = []
        for travels in travelss:
            travel = travels
            if travel.comments.count() < travel.comments.count():
                travel = travels
        serializer = TravelSerializer(travel)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def category_travel(self, request, *args, **kwargs):
        travel = self.get_object()
        category = travel.category
        serializer = TravelCategorySerializer(travel)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def place_travel(self, request, *args, **kwargs):
        travel = self.get_queryset()
        place = travel.place.all()
        serializer = PlacesSerializer(place, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AboutUsAPIViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'name', 'text', 'hotels__name', 'travels__name', 'created_date']

    @action(detail=False, methods=['get'])
    def today_about_us(self, request):
        about = self.get_queryset()
        about = about.filter(created_date__icontains=datetime.now().date())
        serializer = AboutUsSerializer(about, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def total_hotels(self, request, *args, **kwargs):
        about = self.get_object()
        count = 0
        for hotel in about.hotels.all():
            count += 1
        return Response(data=count, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def total_travels(self, request, *args, **kwargs):
        about = self.get_object()
        count = 0
        for travel in about.travels.all():
            count += 1
        return Response(data=count, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def travels(self, request, *args, **kwargs):
        about = self.get_object()
        travels = about.travels
        serializer = TravelSerializer(travels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BookingsAPIViewSet(ModelViewSet):
    queryset = BookNow.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id',
                     'full_name',
                     'email',
                     'persons',
                     'users__first_name',
                     'users__last_name',
                     'users__username',
                     'travel__name',
                     'travel__price',
                     'travel__price_type',
                     'travel__category__name',
                     'travel__places__title',
                     'travel__places__author__employee__first_name',
                     'travel__departure_date',
                     'created_date']

    @action(detail=False, methods=['get'])
    def bookings_count(self, request, *args, **kwargs):
        booking = self.get_queryset()
        user = request.user
        booking = booking.filter(users=user)
        count = booking.count()
        return Response(data=count, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def user(self, request, *args, **kwargs):
        booking = self.get_object()
        user = booking.users
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def travel(self, request, *args, **kwargs):
        booking = self.get_object()
        travel = booking.travel
        serializer = TravelSerializer(travel, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['id', 'username', 'first_name', 'last_name']
