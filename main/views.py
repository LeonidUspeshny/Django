import requests
from django.shortcuts import render
from .models import City

from .forms import CityForm



def index(request):
    return render(request, 'main/index.html',{'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'title': 'О себе'})


def weather(request):
    appid = 'd3b1ff1790a9400c8d6d6aebac929ec5'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': city_info}
    return render(request, 'main/weather.html', context)
