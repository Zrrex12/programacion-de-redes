
import requests

latitud= 19.4450
longitud=-99.1310
clave="d83f6b74e75dbab81417794de8177a57"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data=requests.get(main_api).json()
print(json_data)
print(json_data['name'])