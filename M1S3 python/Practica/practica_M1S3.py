#Calculadora aritmetica
def calculadora_aritmetica(operacion_aritmetica, primer_valor_numerico,segundo_valor_numerico):
    resultado_aritmetico = 0 
    operacion_ejecutada = True
    mensaje = " "
    if operacion_aritmetica == "suma":
        resultado_aritmetico =primer_valor_numerico + segundo_valor_numerico
    elif operacion_aritmetica == "resta":    
        resultado_aritmetico = primer_valor_numerico - segundo_valor_numerico
    elif operacion_aritmetica == "multiplicacion":    
        resultado_aritmetico = primer_valor_numerico * segundo_valor_numerico
    elif operacion_aritmetica == "division":    
        resultado_aritmetico = primer_valor_numerico / segundo_valor_numerico
    else:
        operacion_ejecutada = False
        mensaje = "Opcion invalida"
    
    return { 
        "operacion_aritmetica" : operacion_aritmetica,
        "resultado_aritmetico": resultado_aritmetico,
        "mensaje" : mensaje,
        "operacion_ejecutada": operacion_ejecutada
        }



dato1 = int(input("Ingrese el primer numero: "))
dato2 = int(input("Ingrese el segundo numero: "))
operacion = input("Escriba la operacion: ").lower()
resultado = calculadora_aritmetica(operacion, dato1, dato2)
if resultado["operacion_ejecutada"]:
    print(resultado["resultado_aritmetico"])
else:
     print(resultado["mensaje"])