''' Nombre: Rafael Robles Gonzalez
    Descripcion: Fundamentos Python
    Fecha: 01/11/24'''
    
import requests

url = "https://restcountries.com/v3.1/all"

while True:
    try:
        #Obtener el id por medio de teclado
        xd = input("Ingresa el id del pais (o escribe 'salir'para terminar): ")
        if xd.lower() == 'salir':
            break
        # Convertimos el ID ingresado a un número entero
        id = int(xd)
        # Hacemos la solicitud a la API
        json_data = requests.get(url).json()
        #Mostrar datos
        print(f"Nombre: {json_data[id]['name']['common']}")
        print(f"Capital: {json_data[id]['capital'][0]}")
        print(f"Region: {json_data[id]['region']}")
        print(f"Lenguajes: {json_data[id]['languages']}")

    except ValueError:
        print("Error: Ingresa un número válido para el ID o 'salir' para terminar.")
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
    except IndexError:
        print("Error: ID fuera del rango de países disponibles.")
    except KeyError as e:
        print("Error: La clave", e, "no se encuentra en la respuesta JSON.")
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
