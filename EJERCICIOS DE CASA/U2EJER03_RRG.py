''' Nombre: Rafael Robles Gonzalez
    Descripcion: Fundamentos Python
    Fecha: 01/11/24'''
    
import requests

url = 'https://api.jikan.moe/v4/seasons/2021/winter?sfw'

try:
    response = requests.get(url)
    data = response.json()
    
    while True:
       #Obtener el titulo por medio de teclado
        nombre = input("Dame un titulo de anime (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        encontrado = False
        #verificamos los datos con el uso del ciclo for
        for titulos in data['data']:
           #Si el titulo se encuentra imprimimos los datos
            if nombre == titulos.get('title'):
                print("Tipo: " + str(titulos.get('type')))
                print("Fuente: " + str(titulos.get('source')))
                print("Episodios: " + str(titulos.get('episodes')))
                print("Estatus: " + str(titulos.get('status')))
                encontrado = True
                break
        #Si el titulo no se encuentra se imprime esto
        if encontrado == False:
            print("Título no encontrado en la lista de animes.")

except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)
except ValueError as e:
    print("Error al procesar la respuesta JSON:", e)
except KeyError as e:
    print("Error: La clave", e, "no se encuentra en la respuesta JSON.")
