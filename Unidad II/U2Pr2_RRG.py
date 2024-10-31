import requests

'''Definir una función llamada linea donde se emplee el ciclo for para desplegar una
línea de símbolos tal como lo muestra la siguiente imagen(es a decisión propia el
símbolo). 0.1 puntos'''

'''x=[]
def linea():
    for i in range(10):
        x[i]="*"
    print(x[i])
print(linea())'''

'''Realizar una función en donde se busque el libro 0.2 puntos
e. Parámetro de entrada el título del libro.
f. Verificar que el código de estatus es distinto a 200, enviar el mensaje: Error en la
solicitud'''
def busqueda(llamada):
    url=(f"https://openlibrary.org/search.json?q="+str(llamada))
    codigo=requests.get(url)
    cod=codigo.status_code
    if(cod == 200):
        response=requests.get(url).json()
        return response
        
    else:
        resp=("Error en la solicitud")
        return resp

while True:
    llamada=input("Dame un titulo: ")#the+lord+of+the+rings
    if(llamada == ""):
        print("No puede estar vacio")
        break
    #else:
        #print(busqueda(llamada))
    url=(f"https://openlibrary.org/search.json?q="+str(llamada))    
    datos=requests.get(url).json()
    for documento in datos['docs']:
        print(documento['title'])
    
    titulo=input("Elige un titulo: ")
    for documento in datos['docs']:
        #print(documento)
        if (titulo == documento['title']):
            print("Titutlo: "+str(documento['title']))
            #print("Autor: "+str(documento['author_name'][0]))
            print("Año de publicacion: "+str(documento['first_publish_year']))
            print("Mas informacion: "+url)
            break