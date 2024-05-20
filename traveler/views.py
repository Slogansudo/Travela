from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import (Gallery, Country, City, Address, Hotels, TravelCategory, PlaceCategories,
AboutUs, Places, Team, Travels, Comments, BookNow)


class HomePageView(View):
    def get(self, request):
        about = AboutUs.objects.all()
        if not about:
            aboutus = None
        else:
            aboutus = AboutUs.objects.latest('id')
        cities = City.objects.all()
        places = Places.objects.all()
        place_categories = PlaceCategories.objects.all()
        travelcategories = TravelCategory.objects.all()
        travels = Travels.objects.all()
        booknow = BookNow.objects.all()

        context = {
            'aboutus': aboutus,
            'places': places,
            'cities': cities,
            'travelcategories': travelcategories,
            'travels': travels,
            'place_categories': place_categories,
            'booknow': booknow,
        }
        return render(request, 'travel/index.html', context)

    def post(self, request):
        search = request.POST.get('search')
        if search == 'chegirma':
            about = AboutUs.objects.all()
            if not about:
                aboutus = None
            else:
                aboutus = AboutUs.objects.latest('id')

            cities = City.objects.all()
            places = Places.objects.all()
            place_categories = PlaceCategories.objects.all()
            travelcategories = TravelCategory.objects.all()
            travelss = Travels.objects.all()
            travels = []
            for travel in travelss:
                if travel.discounts != 0:
                    travels.append(travel)
            booknow = BookNow.objects.all()
            context = {
                'aboutus': aboutus,
                'places': places,
                'cities': cities,
                'travelcategories': travelcategories,
                'travels': travels,
                'place_categories': place_categories,
                'booknow': booknow,
            }
            return render(request, 'travel/index.html', context)
        else:
            about = AboutUs.objects.all()
            if not about:
                aboutus = None
            else:
                aboutus = AboutUs.objects.latest('id')
            cities = City.objects.filter(name__icontains=search)
            if not cities:
                cities = City.objects.all()
            places = Places.objects.filter(title__icontains=search)
            if not places:
                places = Places.objects.all()
            place_categories = PlaceCategories.objects.all()
            travelcategories = TravelCategory.objects.all()
            travels = Travels.objects.filter(name__icontains=search)
            if not travels:
                travels = Travels.objects.all()
            booknow = BookNow.objects.all()
            context = {
                'aboutus': aboutus,
                'places': places,
                'cities': cities,
                'travelcategories': travelcategories,
                'travels': travels,
                'place_categories': place_categories,
                'booknow': booknow,
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
        if len(password1) < 4:
            return render(request, 'auth/register_user.html', {'comment': 'at least 4 characters'})
        if password1 != password2:
            return render(request, 'auth/register_user.html', {'comment': 'The password was entered incorrectly'})
        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username) == 0:
            return render(request, 'auth/register_user.html', {'comment': 'fields must be filled'})
        users = User.objects.filter(username=username)
        if not users:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('landing')
        else:
            return render(request, 'auth/register_user.html', {'comment': 'The following user exists'})


class UserProfileView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return render(request, 'travel/profile.html', {'user': user})


class UserAccountDeleteView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return redirect('landing')


class UserProfileEditView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        booknow = BookNow.objects.filter(users=request.user)
        return render(request, 'travel/settings_acount.html', {'user': user})


    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(password1) < 4:
            return render(request, 'travel/settings_acount.html', {'comment': 'Password must be at least'})
        if password1 != password2:
            return render(request, 'travel/settings_acount.html', {'comment': 'The password was entered incorrectly'})
        else:
            users = User.objects.get(username=username)
            user = request.user
            if users != user:
                if not users:
                    user.username = username
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(password1)
                    user.save()
                    return render(request, 'travel/settings_acount.html', {'user': request.user, 'comment': 'succesfull'})
                else:
                    return render(request, 'travel/settings_acount.html',{'comment': 'such username exists'})
            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.set_password(password1)
                user.save()
                user = User.objects.get(username=username)
                return render(request, 'travel/settings_acount.html', {'user': user, 'comment': 'succesfull'})


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        booknow = BookNow.objects.filter(users=request.user)
        context = {
            'booknow': booknow,
        }
        return render(request, 'travel/contact.html')
