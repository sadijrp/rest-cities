import os

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import City
from .serializers import CitySerializer
from .csv_utils import read_cities_from_file
from django.conf import settings


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


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
