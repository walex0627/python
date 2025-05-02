"""contadores_mayores_0 = 0
cantidad_ingresada = 0
cantidad_objetivo = 10

for i in range(10):
    cantidad_ingresada = int(input("Ingresa un numero: "))
    if cantidad_ingresada >= 0:
        contadores_mayores_0+= 1


    
print(f"Los numeros ingresados son {cantidad_ingresada} y los numeros positivos a 0 son {contadores_mayores_0}")"""

#2 Sumatoria hasta alcanzar un minimo 

"""suma = 0  # Inicializamos la variable para almacenar la suma en 0

while suma <= 100:  # El bucle continúa mientras la suma sea menor o igual a 100
    try:
        numero_ingresado = int(input("Ingrese un número: "))  # Pedimos al usuario que ingrese un número y lo convertimos a entero
        suma += numero_ingresado  # Añadimos el número ingresado a la suma total
        print(f"Suma actual: {suma}")  # Mostramos la suma actual (opcional, pero útil para ver el proceso)
    except:
        print("¡Entrada inválida! Por favor, ingrese un número entero.")

print(f"¡La suma ha superado 100! La suma final es: {suma}")
"""
#3 Generador de tabla de multiplicar
"""try:
    numero  = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # El bucle se ejecutará desde 1 hasta 10 (inclusive)
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except: 
    print("Ingrese un numero valido")"""

#4 Contador de intentos
"""
numero_correcto = 8
limite_intentos = 5
intentos = 0
print("ADIVINA EL NUMERO CORRECTO")
print(f"Solo tienes {limite_intentos} intentos")

while intentos < limite_intentos:
    try:
        numero_ingresado = (int(input("Adivina el numero del 1 al 10: ")))
        intentos += 1
        print(f"Haz realizado {intentos} intentos")

        if numero_ingresado == numero_correcto:
            print(f"¡Adivinaste el numero, el numero es {numero_correcto}")
    except: 
        print("Ingrese un valor valido.")"""

#5 Verificador de edad
"""print("--------VERIFICADOR DE EDAD--------")
print("¿Eres mayor de edad?")
print("\nElige una opcion (Solo numeros) \n1 = Si\n2 = No\n")
edad = int(input("Tu opcion seleccionada es:\n"))
while True:
    if edad == 1:
        anos = int(input("Cuantos años tienes?:\n"))
        if anos >= 18:
            print("---Enhorabuena, tienes acceso---")
        else:
            print("---Acceso Denegado---")
        break
    else:
        print("No tienes acceso.")
        break"""
#6


