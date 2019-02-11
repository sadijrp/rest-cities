from django.db import models


class City(models.Model):
    ibge_id = models.IntegerField()
    uf = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    capital = models.BooleanField()
    lon = models.DecimalField(decimal_places=15, max_digits=20)
    lat = models.DecimalField(decimal_places=15, max_digits=20)
    no_accents = models.CharField(max_length=100)
    alternative_names = models.CharField(max_length=100)
    microregion = models.CharField(max_length=100)
    mesoregion = models.CharField(max_length=100)

    def __str__(self):
        return self.ibge_id + ' - ' + self.name
