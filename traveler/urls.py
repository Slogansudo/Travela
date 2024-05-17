from django.urls import path
from .views import HomePageView, UsersLoginView, UserRegisterView, UsersLogoutView


urlpatterns = [
    path('', HomePageView.as_view(), name='landing'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UsersLogoutView.as_view(), name='logout')
]
