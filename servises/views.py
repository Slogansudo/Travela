from django.shortcuts import render
from django.views import View


# Create your views here.


class AboutUsView(View):
    def get(self, request):
        return render(request, 'travel/about.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'travel/services.html')


class BlogsView(View):
    def get(self, request):
        return render(request, 'travel/blog.html')
