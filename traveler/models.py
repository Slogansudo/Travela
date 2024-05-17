from django.db import models
from django.contrib.auth.models import User
from .helps import EmployeStatus, SaveMediafile, PriceType

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=SaveMediafile.save_city_media)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Team(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=EmployeStatus.choices, default=EmployeStatus.other)
    image = models.ImageField(upload_to=SaveMediafile.save_employe_image)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=SaveMediafile.save_gallery_media)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Hotels(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    images = models.ManyToManyField(Gallery, related_name='hotels_gallery', blank=True)
    price = models.FloatField()
    service_term = models.IntegerField(default=1)
    discount = models.FloatField(default=0)
    price_type = models.CharField(max_length=20, choices=PriceType.choices, default=PriceType.usa)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class PlaceCategories(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Places(models.Model):
    author = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    hotels = models.ManyToManyField(Hotels, related_name='places_hotels', blank=True)
    images = models.ManyToManyField(Gallery, related_name='places_gallery', blank=True)
    category = models.ForeignKey(PlaceCategories, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class TravelCategory(models.Model):
    author = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=SaveMediafile.save_tour_category_media)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class Travels(models.Model):
    name = models.CharField(max_length=100)
    persons = models.IntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PriceType.choices, default=PriceType.usa)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediafile.save_travel_media)
    category = models.ForeignKey(TravelCategory, on_delete=models.CASCADE)
    places = models.ManyToManyField(Places, related_name='places')
    discounts = models.FloatField(default=0)
    departure_date = models.DateTimeField(auto_created=True)
    return_day = models.DateTimeField(auto_created=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]


class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=SaveMediafile.save_about_us_media)
    hotels = models.ManyToManyField(Hotels, related_name='hotels')
    travels = models.ManyToManyField(Travels, related_name='travels')
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

