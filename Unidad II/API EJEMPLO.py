import requests
import time
while True:
    id = input("Ingresa el producto con su ID: ")
    if id == 'salir' or id == 's':
        break
    url=f'https://fakestoreapi.com/products/'
    productos=requests.get(url).json()

    #for prod in productos.json():
    print(productos['title'],'\t', productos['price'])
    time.sleep(2)
