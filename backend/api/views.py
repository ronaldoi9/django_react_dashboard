from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CulinarySerializer, StatesAndCitiesSerializer
from .models import Culinary, StatesAndCities
import os, json

class CulinaryViewSet(viewsets.ModelViewSet):
    queryset = Culinary.objects.all()
    serializer_class = CulinarySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = StatesAndCities.objects.all()
    serializer_class = StatesAndCitiesSerializer

def registerStateAndCitiesOnDataBase(request):
    path = os.path.dirname(os.path.abspath(__file__))
    path = path.replace('/api', '/')
    
    json_file = open(f'{path}/estados-cidades.json', 'r')
    json_data = json.load(json_file)
    
    cont = 1
    for state in json_data['estados']:      
        state_sigla = state['sigla']
        state_name = state['nome']

        cities_list = []
        for city in state['cidades']:
            cities_list.append(city)

        save_in_data_base = StatesAndCities(cont, state_sigla, state_name, cities_list)
        save_in_data_base.save()
        cont = cont + 1    

    return HttpResponse('Estados e cidades registrados com sucesso no banco!')