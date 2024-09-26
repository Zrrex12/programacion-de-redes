''' Nombre: Rafael Robles Gonzalez
    Descripcion: palindromos
    Fecha: 23 de septiembre'''
palabra=input("")
word = palabra[::-1]
if palabra == word:
    print("SI")
else:
    print("NO")