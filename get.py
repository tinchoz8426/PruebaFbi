import requests
import json

# API del FBI
response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)
# print(data['total'])
print(data["items"][0]["images"][0]["original"])
# Lo podemos acomodar un poquito para que quede mas legible y poder trabajar mejor
""" json_object = json.dumps(data, indent = 4) 
print(json_object) """

# API de geolocalizacion
""" response = requests.get('http://ip-api.com/json/152.168.182.81')
data = json.loads(response.content)
print(data) """

# A trabajar!!
"A LABURAR!!!" "VAN A TRAER INFORMACION DESDE UN SITIO WEB POR PRIMERA VEZ"
""" response = requests.get('https://dog.ceo/api/breeds/image/random')
data = json.loads(response.content)
print(data) """


with open("fbi.json", "w") as file:
    json.dump(data, file, indent=4)
