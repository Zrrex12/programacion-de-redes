''' Nombre: Rafael Robles Gonzalez
    Descripcion: Las edades cluberas
    Fecha: 23 de septiembre'''
edades_str = input()
edades = [int(edad) for edad in edades_str.split()]
edades_unicas = set(edades)
edades_ordenadas = sorted(edades_unicas, reverse=True)
edades_str_final = [str(edad) for edad in edades_ordenadas]

print(edades_str_final)