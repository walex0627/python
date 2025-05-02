#Presentacion del calculador de notas
print("------Ingrese sus calificaciones.------")
print("Las calificaciones deben ser del 1 al 100.")

#Lista para las calificaciones de la opcion 1
calificaciones = []

#Pregunta para saber que metodo eligira para digitar las notas
#"while" y "try" para cuando se ingrese una opcion invalida se repita el ciclo y muestre que deba ingresar una opcion especifica
"""opcion = int(input("\n¿Como prefieres registrar las notas?\n1. Una por una\n2. Separadas por comas\n"))"""
while True:
    try:
        opcion = int(input("\n¿Como prefieres registrar las notas?\n1. Una por una\n2. Separadas por comas\n"))
        if opcion == 1 or opcion == 2:
            print("\nElige una opcion correcta.\n")
            break
        else:
            print("Elige una opcion valida")
    except:
        print("\nIngrese un valor valido.\n")
#Utilizo el condicional "if" para la opcion 1
if opcion == 1:
    #Utilizo el ciclo "while" para que a la hora de ingresar un numero negativo se reinicio el ciclo
    #Utilizo el "try" y "except" para que a la hora de ingresar un "str" le de error y vuelva a preguntar
    while True:
        try:
            #Le do
            cantidad_calificaciones = int(input("¿Cuántas calificaciones desea agregar?\n "))
            if cantidad_calificaciones > 0:
                break  
            else:
                print("Por favor, ingrese un número positivo de calificaciones.")
        except ValueError:
            print("Ingrese un valor numérico válido para la cantidad.")
    #Utilizo el ciclo "for" para que pregunte las veces que se indique en la variable "calificacion"
    # y enumere cada "input" con el numero de la nota correspondiente
    #Se repite la implementacion de "while" para solo ingresar numeros positivos y "try" para que no acepte "str"
    for i in range(cantidad_calificaciones):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificacion numero {i+1}: "))
                if 0 <= calificacion and calificacion <= 100:
                    calificaciones.append(calificacion)
                    if calificacion <= 50:
                        print(f"Esta calificacion esta reprobada.")
                    else:
                        print(f"Esta calificacion esta aprobada.")    
                    break  
                else:
                    print("La calificación debe estar entre 1 y 100.")
            except ValueError:
             print("Ingrese un valor numérico válido para la cantidad.")   
    print(f"\nLas calificaciones ingresadas son:\n{calificaciones}")
    suma_calificaciones = sum(calificaciones)
    promedio_calificaciones = (suma_calificaciones/cantidad_calificaciones)
    print(f"Tu promedio de notas es {promedio_calificaciones:.2f} ")
  
   # Utilizo el "while" para solo ingresar numeros positvos y "try" para que no acepte "str"
   #La variable "pregunta_calificaciones" para saber cuales notas estan por encima del valor ingresado 
   #Utilizo el "if" para que solo acepte numeros entre 0 y 100
   #Muestra las notas superiores
   # Utilizo "for" para que muestre "numero" de la lista "calificaciones"
   # "if" para que muestre todos los numeros mayores al ingresado en "pregunta_calificaciones" 
    while True :
        try: 
            pregunta_calificaciones = float(input("\nIngresa una calificacion para saber cuales notas estan por encima de este:\n"))
            if 0 <= pregunta_calificaciones <= 100:
                    print(f"\nEstas calificaciones estan por encima del numero {pregunta_calificaciones}:\n ")
                    for numero in calificaciones:
                        if numero > pregunta_calificaciones:
                            print(numero)
            else: 
                print("Ingresa un numero entre 0 y 100.")
        except ValueError:
            print("Ingrese un valor numerico entero.")

        # Utilizo el "while" para solo ingresar numeros positvos y "try" para que no acepte "str"
        # le doy un valor a "calificaciones buscadas" y "calificaciones_repetidas"
        #Utilizo ".count()" para contar en la lista el valor de la variable "calificaciones_buscadas"
        #Utilizo "if", "elif" y "else" para que que si se cumple esa condicion imprima un mensaje
        #Donde muestre la calificacion buscada y las veces q se repite
        while True:
            try:
                calificaciones_buscadas = int(input("\nIngresa una calificacion para saber cuantas veces se repite:\n"))
                calificaciones_repetidas = calificaciones.count(calificaciones_buscadas)
                if 0 <= calificaciones_buscadas <= 100:
                    if calificaciones_repetidas < 0:
                        print("Ingrese un valor entre 0 y 100") 
                    elif calificaciones_repetidas == 0:
                        print(f"\nLa calificacion {calificaciones_buscadas} se repite {calificaciones_repetidas} veces")
                        break
                    elif calificaciones_repetidas== 1 :
                        print(f"\nLa calificacion {calificaciones_buscadas} se repite {calificaciones_repetidas} vez")
                        break
                    else:
                        print((f"\nLa calificacion {calificaciones_buscadas} se repite {calificaciones_repetidas} veces"))
                        break
                else:
                    print("Ingrese un valor numerico entre 0 y 100")
            except ValueError:
                print("Ingrese un valor numerico valido para la busqueda de repeticiones.")
# "elif" para la segunda opcion
# Le doy un valor a "notas", "notas_separadas","conversion", "cantidad_notas", "suma_notas" y "promedio_notas"
# "notas.split(" , ")" es para separar el texto str y me coloque aparte cada nota numero que se ingrese
# "[float(n.strip()) for n in notas_seperadas]" para realizar la conversion de str a float y creo en esta la lista "conversion"
# "len(notas_seperadas)" para contar el numero de objetos totales en la lista "conversion"
# "sum(conversion)" la utilizo para sumar todos los numeros que estan en la lista
# Le doy valor a "promedio_notas" que es el calculo para sacar el promedio
# Imprime las notas ingresadas y el promedio de las notas
elif opcion == 2:
    notas = (input("Registra las notas separadas por comas: "))
    notas_seperadas = notas.split(",")
    conversion = [float(n.strip()) for n in notas_seperadas]
    cantidad_notas = len(notas_seperadas)
    suma_notas = sum(conversion)
    promedio_notas = (suma_notas/cantidad_notas)
    print(f"\nLas calificaciones ingresadas son:\n{conversion}")
    print(f"Tu promedio de notas es {promedio_notas:.2f} ")

    # Utilizo el "while" para solo ingresar numeros positvos y "try" para que no acepte "str"
    # "preguntas_notas" le doy valor para que el dato ingresado sea "int"
    # "if" para que muestre todos los numeros mayores al ingresado en "pregunta_notas"  
    while True:
            try:
                pregunta_notas = int(input("\nIngresa un numero para saber cuantas notas son mayores que este:\n"))
                if pregunta_notas >= 0 and pregunta_notas <= 100:
                    print(f"\nEstas calficaciones estan por encima del numero {pregunta_notas} son:\n ")
                    for numero in conversion:
                        if numero > pregunta_notas:
                            print(numero)
                    break
                else:
                    print("Ingrese un valor nentre 0 y 100.")        
            except ValueError:
                print("Ingrese un numero valido para la busqueda de notas")
    
    # Utilizo el "while" para solo ingresar numeros positvos y "try" para que no acepte "str"
    # le doy un valor a "notas_buscadas" y "notas_repetidas"
    #Utilizo ".count()" para contar en la lista el valor de la variable "conversion"
    #Utilizo "if", "elif" y "else" para que que si se cumple esa condicion imprima un mensaje
    #Donde muestre la calificacion buscada y las veces q se repite
    while True:
        try:           
            notas_buscadas = int(input("\nIngresa un numero para saber cuantas veces se repite:\nDebe estar entre 0 y 100\n"))
            notas_repetidas = conversion.count(notas_buscadas)
            if 0 <= notas_buscadas <= 100:

                if notas_repetidas== 1 :
                    print(f"\nLa calificacion {notas_buscadas} se repite {notas_repetidas} vez")
                    break
            elif notas_repetidas== 0 :
                print(f"\nLa calificacion {notas_buscadas} se repite {notas_repetidas} veces")
                break
            else:
                print((f"\nLa calificacion {notas_buscadas} se repite {notas_repetidas} veces"))
                break
        except:
            print("Ingrese un valor numerico entre 1 y 100 para la busqueda de repeticiones de notas.")
else:
    print("\nElija una opcion correcta\n")
print("¡Gracias por ingresar sus calificaciones!")