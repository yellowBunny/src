from django.shortcuts import render
from django.http import HttpResponse
from src.sensors import virtual_DHT11, virtual_ds18b20, container_temp, static_container
import json, os

STATIC_TEMP_FILE = 'sensors/temp.json'

def home(request):
    return render(request, 'home.html', {})

def temp(request):
    sensor = virtual_DHT11.DHT11()
    temp_salon = sensor.json_temp(10)
    temp_p1 = sensor.json_temp(20)
    temp_p2 = sensor.json_temp(21)
    temp_kitchen = sensor.json_temp(22)
    temp_bathroom = sensor.json_temp(23)
    return render(request, 'temp.html', {'temp_salon': temp_salon, 'temp_p1': temp_p1, 'temp_p2' : temp_p2,
                                         'temp_kitchen' : temp_kitchen, 'temp_bathroom': temp_bathroom},)

def sockets(request):
    all_temps = container_temp.Container().temp_containter_list()
    return render(request, 'sockets.html', {})


def back(request):
    print('jestes w views.back')
    print(os.getcwd())
    container = container_temp.Container().temp_containter_list()
    temp_in_json = static_container.KeepTempInFile().read_from_json(STATIC_TEMP_FILE)
    print(temp_in_json)
    print(container)

    json_data = json.JSONEncoder().encode(container)
    return HttpResponse(json_data)





