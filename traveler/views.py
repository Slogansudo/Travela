from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import (Gallery, Country, City, Address, Hotels, TravelCategory, PlaceCategories,
AboutUs, Places, Team, Travels)


class HomePageView(View):
    def get(self, request):
        aboutus = AboutUs.objects.latest('id')
        cities = City.objects.all()
        places = Places.objects.all()
        place_categories = PlaceCategories.objects.all()
        travelcategories = TravelCategory.objects.all()
        travels = Travels.objects.all()
        context = {
            'aboutus': aboutus,
            'places': places,
            'cities': cities,
            'travelcategories': travelcategories,
            'travels': travels,
            'place_categories': place_categories,
        }
        return render(request, 'travel/index.html', context)


class UsersLoginView(View):
    def get(self, request):
        return render(request, 'auth/login_users.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'auth/login_users.html')


class UsersLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing')


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register_user.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')
