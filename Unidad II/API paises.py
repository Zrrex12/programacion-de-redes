import requests

url = "https://restcountries.com/v3.1/all"
while True:
    id = int(input("Ingresa el id del pais: "))
    if id == 'salir' or id == 's':
        break
    json_data = requests.get(url).json()
    print(f"Nombre: {json_data[id]["name"]["common"]}")
    print(f"Capital: {json_data[id]["capital"][0]}")
    print(f"Region: {json_data[id]["region"]}")
    print(f"Lenguajes: {json_data[id]["languages"]}")