''' Nombre: Rafael Robles Gonzalez
    Descripcion: Manejo de colecciones
    Fecha: 03/10/24'''
#Escribe la instrucción para agregar una colección vacía con el nombre de tu grupo.
GIR0641 = {}
#Crea una lista llamada numeros_control e inicialízala con cinco números de control de tus compañeros. Véase la siguiente figura
numeros_control = [1223100471, 1223100472, 1223100473, 1223100474, 1223100475]
#Escribe la instrucción que imprima todo el contenido de la lista.
print(numeros_control)
#Mediante un foreach que itera la lista de los números de control
for numcontrol in numeros_control:
    #a. Solicite los nombres de los estudiantes de acuerdo al número control
    print("Ingresa el nombre del No. Control", numcontrol)
    #b. Mediante la función input solicite el nombre
    nombre = input("Ingresa el nombre: ")
    #Una vez que se capture el nombre agrega el dato a la colección haciendo corresponder el número de control con el nombre
    GIR0641[numcontrol]=nombre;
#Imprime el contenido de la colección.
print(GIR0641)
#Escribe un ciclo infinito que busque en la colección un número de control existente
while True:
    #Solicita el número de control con la función input.
    numero_control = input("Ingresa el número de control: ")
    numero_control = int(numero_control)
    # Con la condicional SI-ENTONCES-SINO cuestiona si existe el número de control en la colección
    if numero_control in GIR0641:
        # En caso afirmativo, despliega el nombre de acuerdo al número de control y con la instrucción break rompe el ciclo while
        print(f"El nombre del estudiante es: {GIR0641[numero_control]}")
        break
    else:
        #En caso contrario, despliega el mensaje “El número de control no fue encontrado  inténtalo Otra vez”
        print("El número de control no fue encontrado. Inténtalo otra vez.")
    