import requests
import json


response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Paris,fr&appid=281f2f47a07f35357ba3cefcc47c7f52&units=metric&mode=json")

print(response)
print(type(response))

print(response.text)
print(type(response.text))

"""
#Exemple tiré de https://docs.python.org/fr/3/library/json.html :

json_décodé = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(json_décodé)
print(type(json_décodé))

print('["foo", {"bar":["baz", null, 1.0, 2]}]'[1])
mon_dict = json_décodé[1]
print(mon_dict)
print('mon_dict vaut : ' + str(mon_dict))

print(mon_dict['bar'])
ma_liste = mon_dict['bar']

print(ma_liste[2])
print(json_décodé[1]['bar'][2])
"""

json_décodé = json.loads(response.text)
print(json_décodé)
print(json_décodé['main']['temp'])
print(json_décodé['weather'][0]['description'])

