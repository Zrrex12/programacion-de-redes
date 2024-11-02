''' Nombre: Rafael Robles Gonzalez
    Descripcion: Fundamentos Python
    Fecha: 01/11/24'''
    
import requests

url = 'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=IBM&apikey=GRRKF4OAUQ1AWSU0'

while True:
    try:
        #Obtener el id por medio de teclado
        xd = input("Ingresa el id (o escribe 'salir'): ")
        if xd.lower() == 'salir':
            break
        # Convertimos el ID ingresado a un número entero
        id = int(xd)
        # Hacemos la solicitud a la API
        json_data = requests.get(url).json()
        #Mostrar datos
        print(f"symbol: {json_data['data'][0]['symbol']}")
        print(f"type: {json_data['data'][0]['type']}")
        print(f"contractID: {json_data['data'][0]['contractID']}")

    except ValueError:
        print("Error: Ingresa un número válido para el ID o 'salir' para terminar.")
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
    except IndexError:
        print("Error: El JSON de respuesta no contiene los datos esperados.")
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
