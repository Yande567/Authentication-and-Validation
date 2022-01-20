from cities_light.receivers import connect_default_signals
from django.db import models
from cities_light.abstract_models import (
    AbstractCity,
    AbstractRegion,
    AbstractCountry,
    AbstractSubRegion)


# Create your models here.
class Country(AbstractCountry):
    name_ascii = models.CharField(max_length=200, default='Zambia')
    slug = models.CharField(max_length=200, default='Zambia')
    continent = models.CharField(max_length=200, default='Zambia')
    tld = models.CharField(max_length=5, default='zm')
    pass


connect_default_signals(Country)


class Region(AbstractRegion):
    name_ascii = models.CharField(max_length=200, default='province')
    display_name = models.CharField(max_length=200, default='province')
    pass


connect_default_signals(Region)


class City(AbstractCity):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default='country_name')
    display_name = models.CharField(max_length=200, default='city,region,country')
    slug = models.CharField(max_length=50, default='city-region')
    timezone = models.CharField(max_length=40, default='Africa/Lusaka')
    name_ascii = models.CharField(max_length=40, default='city')
    search_names = models.CharField(max_length=40, default='city')


connect_default_signals(City)

class SubRegion(AbstractSubRegion):
    name_ascii = models.CharField(max_length=200, default='district')
    name = models.CharField(max_length=200, default='district')
    slug = models.CharField(max_length=200, default='district-province')
    display_name = models.CharField(max_length=200, default='district_name-district')
    pass


connect_default_signals(Region)


class Address(models.Model):
    email = models.EmailField(max_length=35, null=True, blank=True)
    residential_area = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    house_number = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default='Zambia')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default='Province')
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='Town')

    def __str__(self):
        return self.email
