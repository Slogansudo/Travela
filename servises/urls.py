from django.urls import path
from .views import AboutUsView, ServicesView, BlogsView

urlpatterns = [
    path('about/', AboutUsView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
]