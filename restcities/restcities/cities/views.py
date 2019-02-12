
import os
from django.db.models import Count, Max

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City
from .csv_utils import read_cities_from_file
from django.conf import settings
from .serializers import (CitySerializer, CitiesCounterSerializer,
                          CitiesCounterSerializer, StatesCitiesSerializer)


class CityViewSet(viewsets.ModelViewSet):
    """
    Endpoint para retornar as cidades
    """
    queryset = City.objects.filter(capital=True).order_by('name')
    serializer_class = CitySerializer

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(ibge_id=pk)
        serializer = CitySerializer(queryset, many=True)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            instance = City.objects.get(ibge_id=pk)
            self.perform_destroy(instance)
            response_status = status.HTTP_200_OK
        except:
            response_status = status.HTTP_204_NO_CONTENT

        return Response(status=response_status)


class CapitalsViewSet(viewsets.ModelViewSet):
    """
    Endpoint para retornar as capitais ordenadas pelo nome
    """
    queryset = City.objects.filter(capital=True).order_by('name')
    serializer_class = CitySerializer


class StateCitiesCounterViewSet(viewsets.ModelViewSet):
    """
    Endpoint para retornar o número de cidades por estado
    """
    queryset = City.objects.values('uf').annotate(count=Count('pk'))
    serializer_class = CitiesCounterSerializer


class StateCitiesViewSet(viewsets.ModelViewSet):
    """
    Endpoint para retornar as cidades de um determinado estado
    """
    serializer_class = StatesCitiesSerializer

    def get_queryset(self):
        uf = self.kwargs['uf']
        queryset = City.objects.filter(uf=uf)

        return queryset


class CitiesCounterViewSet(viewsets.ModelViewSet):
    """
    Endpoint para retornar a quantidade de cidades
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request):
        count = self.queryset.count()
        return Response({'count': count})


@api_view(['POST'])
def ImportCitiesView(request):
    """
    Endpoint responsável por adicionar as cidades do arquivo cities.csv
    ao banco de dados
    """
    file_path = ".restcities/cities/static/cities.csv"
    file_path = os.path.join(settings.STATIC_ROOT, 'cities.csv')
    delimiter = ','

    file_cities = read_cities_from_file(file_path, delimiter)
    if len(file_cities) == 0:
        msg = "Ocorreu um erro ao processar o arquivo CSV."
    else:
        num_cities = 0
        for city in file_cities:
            City.objects.create(**city)
            num_cities += 1

        msg = "Arquivo processado com sucesso. {0} cidades adicionadas à base"
        msg = msg.format(num_cities)

    response = {
        "message": msg
    }

    return Response(response)
