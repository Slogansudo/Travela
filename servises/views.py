from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from traveler.models import (Gallery, Country, City, Address, Hotels, TravelCategory, PlaceCategories,
AboutUs, Places, Team, Travels, Comments, BookNow)


# Create your views here.


class AboutUsView(View):
    def get(self, request):
        aboutus = AboutUs.objects.all()
        if aboutus:
            aboutus = AboutUs.objects.latest('id')
        else:
            aboutus = None
        teams = Team.objects.all()
        return render(request, 'travel/about.html', {'aboutus': aboutus, 'teams': teams})

    def post(self, request):
        search = request.POST.get('search')
        aboutus = AboutUs.objects.all()
        if aboutus:
            aboutus = AboutUs.objects.latest('id')
        else:
            aboutus = None
        teams = Team.objects.filter(employee__first_name__icontains=search)
        print(teams)
        if not teams:
            teams = Team.objects.filter(employee__last_name__icontains=search)
            if not teams:
                teams = Team.objects.filter(status__icontains=search)
                if not teams:
                    teams = Team.objects.filter(employee__first_name__icontains=search)
                    if not teams:
                        teams = Team.objects.filter(employee__username__icontains=search)
        return render(request, 'travel/about.html', {'aboutus': aboutus, 'teams': teams})


class ServicesView(View):
    def get(self, request):
        booknow = BookNow.objects.all()
        return render(request, 'travel/services.html', {"booknow": booknow})


class HotelsView(LoginRequiredMixin, View):
    def get(self, request):
        hotels = Hotels.objects.all()
        return render(request, 'travel/hotels.html', {"hotels": hotels})
    def post(self, request):
        search = request.POST.get('search')
        if search != 'chegirma':
            hotels = Hotels.objects.filter(name__icontains=search)
            if not hotels and search.isdigit():
                hotels = Hotels.objects.filter(price=int(search))
                if not hotels:
                    hotels = Hotels.objects.filter(service_term=int(search))
                return render(request, 'travel/hotels.html', {"hotels": hotels})
            else:
                return render(request, 'travel/hotels.html', {"hotels": hotels})
        else:
            hotelss = Hotels.objects.all()
            hotels = []
            for hotel in hotelss:
                if hotel.discount != 0:
                    hotels.append(hotel)
            return render(request, 'travel/hotels.html', {"hotels": hotels})


class HotelDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        hotel = Hotels.objects.get(slug=slug)
        return render(request, 'travel/hotel_detail.html', {"hotel": hotel})


class ExploreTravelView(LoginRequiredMixin, View):
    def get(self, request):
        travels = Travels.objects.all()
        return render(request, 'travel/tour.html', {"travels": travels})

    def post(self, request):
        search = request.POST.get('search')
        if search == 'chegirma':
            travelss = Travels.objects.all()
            travels = []
            for travel in travelss:
                if travel.discounts != 0:
                    travels.append(travel)
            return render(request, 'travel/tour.html', {"travels":travels})
        else:
            travels = Travels.objects.filter(name__icontains=search)
            return render(request, 'travel/tour.html', {"travels": travels})


class BlogsView(LoginRequiredMixin, View):
    def get(self, request):
        travels = Travels.objects.all()
        return render(request, 'travel/blog.html', {"travels": travels})

    def post(self, request):
        search = request.POST.get('search')
        if search == 'chegirma':
            travelss = Travels.objects.all()
            travels = []
            for travel in travelss:
                if travel.discounts != 0:
                    travels.append(travel)
            return render(request, 'travel/blog.html', {"travels": travels})
        else:
            travels = Travels.objects.filter(name__icontains=search)
            if not travels:
                travels = Travels.objects.filter(author__employee__username__icontains=search)
                if not travels:
                    travels = Travels.objects.filter(description__icontains=search)
                    if not travels:
                        travels = Travels.objects.filter(category__name__icontains=search)
                        if not travels:
                            travels = Travels.objects.filter(places__title__icontains=search)
                            if not travels:
                                travels = Travels.objects.filter(departure_date__icontains=search)
                                if not travels and search.isdigit():
                                    travels = Travels.objects.filter(price=search)

            return render(request, 'travel/blog.html', {"travels": travels})


class CityPlacesView(LoginRequiredMixin, View):
    def get(self, request, id):
        city = City.objects.get(id=id)
        address = Address.objects.filter(city__id=city.id).first()
        places = Places.objects.filter(address=address)
        return render(request, 'travel/city_places.html', {'places': places, 'city': city})


class HotelBookingView(LoginRequiredMixin, View):
    def get(self, request, slug):
        hotel = Hotels.objects.get(slug=slug)
        dat = []
        places = Places.objects.filter(hotels=hotel)
        if places:
            for place in places:
                dat.append(place)
            travels = Travels.objects.all()
            travel = ''
            for trav in travels:
                for plac in trav.places.all():
                    if plac in dat:
                        travel = trav
                        return render(request, 'travel/viewplaces.html', {'travel': travel})
            return render(request, 'travel/viewplaces.html', {'travel': None})
        else:
            return render(request, 'travel/viewplaces.html', {'travel': None})


class PlacesView(LoginRequiredMixin, View):
    def get(self, request, slug):
        place = Places.objects.get(slug=slug)
        travels = Travels.objects.all()
        travel = ''
        for trav in travels:
            for plac in trav.places.all():
                if plac == place:
                    travel = trav
        return render(request, 'travel/viewplaces.html', {'travel': travel})


class TravelPlacesView(LoginRequiredMixin, View):
    def get(self, request, slug):
        travel = Travels.objects.get(slug=slug)
        return render(request, 'travel/viewplaces.html', {"travel": travel})


class BookNowView(LoginRequiredMixin, View):
    def get(self, request, slug):
        travel = Travels.objects.get(slug=slug)
        booknow = BookNow.objects.filter(users=request.user)
        return render(request, 'travel/booking.html', {'booknow': booknow, "travel": travel})

    def post(self, request, slug):
        travel = Travels.objects.get(slug=slug)
        booknow = BookNow.objects.filter(users=request.user)
        your_name = request.POST.get('yourname')
        email = request.POST.get('email')
        if not your_name or not email:
            return render(request, 'travel/booking.html', {'booknow': booknow, "travel": travel, 'comment': 'enter correct name and email'})
        persons = request.POST.get('persons')
        if int(persons) > travel.persons:
            return render(request, 'travel/booking.html', {'booknow': booknow, "travel": travel, 'comment': 'there are not enough places'})
        message = request.POST.get('message')
        if not message:
            user = User.objects.get(id=request.user.id)
            full_name = your_name
            booknow = BookNow.objects.create(full_name=full_name, email=email, persons=persons, users=user, travel=travel, total_price=travel.price, price_type=travel.price_type)
            booknow.save()
            travel.persons -= int(persons)
            travel.save()
            travel = Travels.objects.get(slug=slug)
            booknow = BookNow.objects.filter(users=user)
            return render(request, 'travel/booking.html', {'booknow': booknow, 'travel': travel})
        else:
            user = User.objects.get(id=request.user.id)
            full_name = your_name
            comment = Comments.objects.create(text=message, user=user)
            comment.save()
            travel.comments.add(comment)
            travel.save()
            booknow = BookNow.objects.create(full_name=full_name, email=email, persons=persons, users=user,
                                             travel=travel, total_price=travel.price, price_type=travel.price_type)
            booknow.save()
            travel.persons -= int(persons)
            travel.save()
            travel = Travels.objects.get(slug=slug)
            booknow = BookNow.objects.filter(users=user)
            return render(request, 'travel/booking.html', {'booknow': booknow, 'travel': travel})


class BookingDetailView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        booknow = BookNow.objects.filter(users=user)
        return render(request, 'travel/booked.html', {'booknow': booknow})


class DeleteBookedView(LoginRequiredMixin, View):
    def get(self, request, id):
        booknow = BookNow.objects.get(id=id)
        booknow.delete()
        return redirect('booking_detail')




# slug = models.SlugField(verbose_name='Slug', max_length=255)
#path('course/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),