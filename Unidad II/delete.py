import requests
import time

while True:
     id = input('Ingresa el ID de produco a eliminar:')
     if id.lower() == 'salir' or id.lower() =='s':
          break

     url = f"https://fakestoreapi.com/products/{id}"
 
     productos = requests.delete(url).json()
     print("producto eliminado")
     time.sleep(2)
     