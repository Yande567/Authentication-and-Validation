from django.http import JsonResponse
from django.shortcuts import render
from .models import *

from django.views.generic import CreateView
from .forms import AddressForm
from django.urls import reverse_lazy

# Create your views here.


class PersonCreateView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('country_selection')


def country_selection(request):
    try:
        qs = Country.objects.all()
        return render(request, 'profile_setup/country_selection.html', {'qs': qs})
    except Exception as e:
        print(e)
    qs = Country.objects.all()
    return render(request, 'profile_setup/country_selection.html', {'qs': qs})


def get_json_country_data(request):
    qs_val = list(Country.objects.values())
    return JsonResponse({'data': qs_val})


def get_json_province_data(request, *args, **kwargs):
    selected_country = kwargs.get('country')
    obj_models = list(Region.objects.filter(country__name=selected_country).values())
    return JsonResponse({'data': obj_models})


def get_json_city_data(request, *args, **kwargs):
    selected_province = kwargs.get('province')
    obj_models = list(City.objects.filter(region__name=selected_province).values())
    return JsonResponse({'data': obj_models})


# checks if request is an ajax request
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def save_country_info(request):
    try:
        if is_ajax(request=request):
            country = request.POST.get('country')
            country_obj = Country.objects.get(name=country)
            province = request.POST.get('province')
            province_obj = Region.objects.get(name=province)
            city = request.POST.get('city')
            city_obj = City.objects.get(name=city)
            Address.objects.create(country=country_obj, region=province_obj, city=city_obj)
            return JsonResponse({'created': True})
        return JsonResponse({'created': False}, safe=False)
    except Exception as e:
        print(e)
    return JsonResponse({'created': False}, safe=False)
