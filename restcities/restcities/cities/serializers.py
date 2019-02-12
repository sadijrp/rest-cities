
from rest_framework import serializers

from .models import City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('ibge_id', 'uf', 'name', 'capital', 'lon', 'lat',
                  'no_accents', 'alternative_names', 'microregion',
                  'mesoregion')


class CitiesCounterSerializer(serializers.HyperlinkedModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = City
        fields = ('uf', 'count')


class StatesCitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name', )
