"""
    Suma 
    Resta 
    Multiplicacion
    Division
"""
    
numero_1= float(input("ingresa primer número: "))
numero_2 = float(input("ingresa segundo número: "))
operacion = input("Escriba el tipo de operacion: ")


#procesamiento y salida
if operacion == "suma":
    resultado = numero_1+numero_2
   

if operacion == "resta":
    resultado = numero_1-numero_2
    
if operacion == "multiplicacion":
    resultado = numero_1*numero_2

#salida
print(f"El resultado de la operacion {operacion} es: {resultado}")




       