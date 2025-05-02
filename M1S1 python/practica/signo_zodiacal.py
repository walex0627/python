
#Creo la lista de signo zodiacal con las tuplas de laa siguiente manera:
#("nombre del signo",((dia_inicio,dia_fin),(mes_inicio,mes_final)))
signo_zodiacal = [
 ("Capricornio", (22, 12), (19, 1)),
    ("Acuario", (20, 1), (18, 2)),
    ("Piscis", (19, 2), (20, 3)),
    ("Aries", (21, 3), (19, 4)),
    ("Tauro", (20, 4), (20, 5)),
    ("Géminis", (21, 5), (20, 6)),
    ("Cáncer", (21, 6), (22, 7)),
    ("Leo", (23, 7), (22, 8)),
    ("Virgo", (23, 8), (22, 9)),
    ("Libra", (23, 9), (22, 10)),
    ("Escorpio", (23, 10), (21, 11)),
    ("Sagitario", (22, 11), (21, 12)),
]

# Lo que le va a salir al usuario a la hora de ingresar su numero de dia y mes este ultimo que lo coloque en numeros
dia  = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento (en números): "))

#Creo un ciclo con for y les doy un valor a las variables de "inicio" y "fin"
for signo_zodiacal, inicio, fin in signo_zodiacal:
    dia_inicio, mes_inicio = inicio
    dia_fin, mes_fin = fin
    #Coloco todos los escenarios posibles adjuntandolos con or para que si cumple alguno de los requisitos pedidos los clasifico
    if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin) or (mes_inicio < mes_fin and mes > mes_inicio and mes < mes_fin) or (mes_inicio > mes_fin and (mes > mes_inicio or mes < mes_fin)):

        print("Tu signo es:", signo_zodiacal)
        
        

"""      
ciudades = ["madrid", "barcelona", "barranquilla"]
for ciudad in  ciudades:  
    print( ciudad )

"""
"""
Ya mejorado 
#Creo la lista de signo zodiacal con las tuplas de laa siguiente manera:
#("nombre del signo",((dia_inicio,mes_inicio),(dia_fin, mes_fin)))
signos_zodiacales = [
    ("Capricornio", (22, 12), (19, 1)),
    ("Acuario", (20, 1), (18, 2)),
    ("Piscis", (19, 2), (20, 3)),
    ("Aries", (21, 3), (19, 4)),
    ("Tauro", (20, 4), (20, 5)),
    ("Géminis", (21, 5), (20, 6)),
    ("Cáncer", (21, 6), (22, 7)),
    ("Leo", (23, 7), (22, 8)),
    ("Virgo", (23, 8), (22, 9)),
    ("Libra", (23, 9), (22, 10)),
    ("Escorpio", (23, 10), (21, 11)),
    ("Sagitario", (22, 11), (21, 12)),
]

# Lo que le va a salir al usuario a la hora de ingresar su numero de dia y mes este ultimo que lo coloque en numeros
dia  = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento (en números): "))
fecha = mes * 31 + dia

#Creo un ciclo con for y les doy un valor a las variables de "inicio" y "fin"
for signo_zodiacal, fecha_inicio, fecha_fin in signos_zodiacales:
    inicio = fecha_inicio[1] * 31 + fecha_inicio[0]
    fin = fecha_fin[1] * 31 + fecha_fin[0]

    if inicio <= fin:
        if inicio <= fecha <= fin:
            print(f'Tu signo zodiacal es {signo_zodiacal}')
            break
    else:
        if fecha >= inicio or fecha <= fin:
            print(f'Tu signo zodiacal es {signo_zodiacal}')
            break
 """