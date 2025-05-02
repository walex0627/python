"""
ciudades = ["madrid", "barcelona", "barranquilla"]
for ciudad in  ciudades:  
    print( ciudad )
"""
"""
print("")
numeros = [3,9,12,15,18,21,24,27]
umbral = 10

for numero in numeros :
    if numero > umbral:
        print(f"El primer número mayor que {umbral} es {numero}.")
        break
else:
    print(f"Ningun numero de la lista es menor que {umbral} y es {numero}")
"""

"""
while True:
    texto=input("Escribe una palabra: ")
    if texto=="sale boca":
        print("Adios.")
        break
print(f"Escribiste: {texto}")
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"Numero: {numero}")
