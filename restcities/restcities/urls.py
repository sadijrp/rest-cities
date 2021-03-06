"""restcities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restcities.cities import views

router = routers.DefaultRouter()
router.register(r'cidades', views.CityViewSet,
                basename="Cidade")
router.register(r'cidades_por_estado/(?P<uf>[A-Z]{2})',
                views.StateCitiesViewSet,
                basename="Cidades de um Estado")
router.register(r'capitais', views.CapitalsViewSet)
router.register(r'numero_cidades_por_estado', views.StateCitiesCounterViewSet)
router.register(r'quantidade_registros', views.CitiesCounterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('popula-bd/', views.ImportCitiesView)
]
