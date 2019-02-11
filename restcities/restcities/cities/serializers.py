from .models import City
from rest_framework import serializers


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('ibge_id', 'uf', 'name', 'capital', 'lon', 'lat',
                  'no_accents', 'alternative_names', 'microregion',
                  'mesoregion')
