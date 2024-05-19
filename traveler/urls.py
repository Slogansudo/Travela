from django.urls import path
from .views import HomePageView, UsersLoginView, UserRegisterView, UsersLogoutView, UserProfileView, UserProfileEditView, UserAccountDeleteView, ContactView


urlpatterns = [
    path('', HomePageView.as_view(), name='landing'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileEditView.as_view(), name='profile_edit'),
    path('delete/acount/', UserAccountDeleteView.as_view(), name='delete account'),
    path('contact/', ContactView.as_view(), name='contact')

]
