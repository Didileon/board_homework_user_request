from django_filters import FilterSet
from .models import Advert
import django_filters


class AdvertFilter(FilterSet):
   class Meta:

       model = Advert

       fields = {
           # поиск по названию
           'subject': ['icontains'],
           'category': ['exact'],
           'price': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }