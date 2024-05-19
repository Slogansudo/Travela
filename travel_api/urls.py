from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from .views import (CountryAPIViewSet, CityAPIViewSet, AddressAPIViewSet, TeamAPIViewSet, GalleryAPIViewSet,
                    HotelsAPIViewSet, PlaceCategoryAPIViewSet, PlacesAPIViewSet, TravelCategoryAPIViewSet,
                    CommentAPIViewSet, TravelAPIViewSet, AboutUsAPIViewSet, BookingsAPIViewSet, UsersAPIViewSet)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TRAVEL API",
        default_version='v1',
        description="Demo TRAVEL API",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='srmslogan6040@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated, )
)


router = DefaultRouter()
router.register('countries', viewset=CountryAPIViewSet)
router.register('cities', viewset=CityAPIViewSet)
router.register('addresses', viewset=AddressAPIViewSet)
router.register('teams', viewset=TeamAPIViewSet)
router.register('galleries', viewset=GalleryAPIViewSet)
router.register('hotels', viewset=HotelsAPIViewSet)
router.register('place_categories', viewset=PlaceCategoryAPIViewSet)
router.register('places', viewset=PlacesAPIViewSet)
router.register('travel_categories', viewset=TravelCategoryAPIViewSet)
router.register('travels', viewset=TravelAPIViewSet)
router.register('comments', viewset=CommentAPIViewSet)
router.register('about_us', viewset=AboutUsAPIViewSet)
router.register('bookings', viewset=BookingsAPIViewSet)
router.register('users', viewset=UsersAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]

