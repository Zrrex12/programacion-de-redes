''' Nombre: Rafael Robles Gonzalez
    Descripcion: Uso de print
    Fecha: 19 de septiembre'''
#2.1.1.6 LABORATORIO: La función print()
'''
print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")
'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Dando forma a una flecha
    Fecha: 19 de septiembre'''
#2.1.1.19 LABORATORIO: Dando formato a la salida
'''print("     *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****")
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)'''


''' Nombre: Rafael Robles Gonzalez
    Descripcion: El uso del escape "\" en cadenas
    Fecha: 19 de septiembre'''
#2.2.1.11 LABORATORIO: Literales de Python - Cadenas
'''print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Uso de variables y sus indentidades
    Fecha: 19 de septiembre'''
#2.4.1.7 LABORATORIO: Variables
'''juan=3
maria=5
adan=6
juan=int(juan)
maria=int(maria)
adan=int(adan)
print(juan,",",+maria,",",+adan)
total_manzanas=juan+maria+adan
print(total_manzanas)'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Convertir millas a kilometros y viceversa
    Fecha: 19 de septiembre'''
#2.4.1.9 LABORATORIO: Variables, un sencillo convertidor
'''kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Evaluar una expresion usando diferentes operadores y expresiones
    Fecha: 19 de septiembre'''
#2.4.1.10 LABORATORIO: Operadores y expresiones
'''x =  -1
x = float(x)
y=(3*x**3)-(2*x**2)+3*x-1
print("y =", y)'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Calcular cuantos segundos tiene un cierto numero de horas
    Fecha: 19 de septiembre'''
#2.5.1.2 LABORATORIO: Comentarios
'''# este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en Horas: ", a * seconds) # se imprime el numero de segundos en determinado numero de horas

#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
#este el es fin del programa que calcula el numero de segundos en 2 horas
'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Ingresar 2 numeros y ejecutar las 4 operaciones basicas
    Fecha: 19 de septiembre'''
#2.6.1.9 LABORATORIO: Entradas y salidas simples
'''a=2.0 # ingresa un valor flotante para la variable a aquí
b=3.0 # ingresa un valor flotante para la variable b aquí

# muestra el resultado de la suma aquí 
print(a+b)
# muestra el resultado de la resta aquí
print(a-b)
# muestra el resultado de la multiplicación aquí
print(a*b)
# muestra el resultado de la división aquí
print(a/b)

print("\n¡Eso es todo, amigos!")
'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Ejecutar una formula usando correctamente la jerarquia de operadores
    Fecha: 19 de septiembre'''
#2.6.1.10 LABORATORIO: Operadores y expresiones
'''x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.
y=(1/(x+(1/(x+(1/(x+(1/x)))))))
print("y =", y)
'''



''' Nombre: Rafael Robles Gonzalez
    Descripcion: Mostrar la hora de salida de un evento segun una hora y los minutos de duracion
    Fecha: 19 de septiembre'''
#2.6.1.11 LABORATORIO: Operadores y expresiones
'''hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
minutos_totales=mins+dura
minutos_sobrantes=minutos_totales%60

horas_totales=hour+minutos_totales//60

print(str(horas_totales)+":"+str(minutos_sobrantes))'''
