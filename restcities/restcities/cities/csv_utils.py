
from decimal import Decimal
import csv
import os


def read_cities_from_file(file_path, delimiter):
    """
    Recupera as cidades do arquivo CSV indicado, devolvendo uma lista de
    dicionários de cidades
    """
    cities_list = []

    if file_path.strip()[-4:] == '.csv':  # processar apenas arquivos CSV
        try:
            with open(file_path, encoding='UTF-8', newline='') as file:
                reader = csv.reader(file, delimiter=delimiter)
                lines = 0

                for row in reader:
                    if lines != 0:
                        city = {
                            'ibge_id': row[0],
                            'uf': row[1],
                            'name': row[2],
                            'capital': True if row[3] == 'true' else False,
                            'lon': Decimal(row[4]),
                            'lat': Decimal(row[5]),
                            'no_accents': row[6],
                            'alternative_names': row[7],
                            'microregion': row[8],
                            'mesoregion': row[9]
                        }

                        cities_list.append(city)
                    lines += 1
        except FileNotFoundError:
            print("Não foi possível processar o arquivo por inteiro.")
            cities_list = []

    return cities_list
