
def preparar_pollo_a_la_plancha():
    while True:
            presentacion = input("Como quieres el pollo?\n(tiras/normal)\n").lower()
            if presentacion in ["tiras", "normal"]:
                if presentacion == "tiras":
                    return "pollo a la plancha cortado en tiras"
                else:
                    return "pollo a la plancha"
            else:
                print("Elija una de las opciones\n")

  

def preparar_salsa_cesar():
    while True:
        tipo_salsa = input("Quieres la salsa cesar tenga pimienta?\n(si/no)\n").lower()
        if tipo_salsa in ["si", "no"]:
            if tipo_salsa == "si" or tipo_salsa == "no":
                return {
                "sal": "al gusto del chef", 
                "zumo_limon": "10 ml", 
                "pimienta_negra": tipo_salsa
                    }
            else :
                print("Debe elegir si o no")       
        else:
                print("Elija una de las opciones\n")

def preparar_ensalada_cesar():
    presentacion_pollo_ensalada = preparar_pollo_a_la_plancha()
    salsa_cesar_ensalada = preparar_salsa_cesar()
    ensalada = {
        "receta": "cesar",
        "presentacion pollo": presentacion_pollo_ensalada,
        "salsa": salsa_cesar_ensalada,
        "ingredientes": ["lechuga romana", "pan tostado en pedacitos", "queso parmesano", presentacion_pollo_ensalada]
    }
    return ensalada

def preparar_sandwich_pollo():
     presentacion_pollo_sandwich = preparar_pollo_a_la_plancha() 
     salsa_cesar_sandwich = preparar_salsa_cesar()
     sandwich = {
        "receta": "sandwich de pollo",
        "presentacion pollo": presentacion_pollo_sandwich,
        "salsa": salsa_cesar_sandwich,
        "ingredientes": ["pan de ajo", "queso mozzarella", presentacion_pollo_sandwich, "tomate", "maiz"]
    }
     return sandwich


def preparar_wrap_pollo():
    presentacion_pollo_wrap = preparar_pollo_a_la_plancha() 
    salsa_cesar_wrap = preparar_salsa_cesar()
    wrap = {
        "receta": "wrap de pollo",
        "presentacion pollo": presentacion_pollo_wrap,
        "salsa": salsa_cesar_wrap,
        "ingredientes": ["tortilla", "queso cheddar", presentacion_pollo_wrap, "maiz dulce", "pico de gallo"]
    }
    return wrap

def emplatado(receta):
    if receta == "ensalada cesar con pollo":
        return preparar_ensalada_cesar()
    elif receta == "wrap de pollo":
        return preparar_wrap_pollo()
    elif receta == "sandwich de pollo":
        return preparar_sandwich_pollo()
    else:
        return {"error": "Receta no encontrada"}
    
print("MENU DE RESTAURANTE")
print("===================")
while True:
    try:
        opcion_plato = int(input("Que vas a pedir?\n1. Ensalada cesar\n2. Sandwich de pollo\n3. Wrap de pollo\nElige por el numero de las opciones:\n"))
        if opcion_plato == 1:
            ensalada_cesar = preparar_ensalada_cesar()
            print("\nPreparando ensalada\n")
            print(ensalada_cesar)
        elif opcion_plato == 2:
            sandwich_pollo = preparar_sandwich_pollo()
            print("\nPreparando sandwich de pollo\n")
            print(sandwich_pollo)
        elif opcion_plato == 3:
            wrap_pollo = preparar_wrap_pollo()
            print("\nPreparando wrap de pollo\n")
            print(wrap_pollo)
        else:
            print("Opcion no valida.")
        break
    except ValueError:
        print("Ingrese un numero dentro de los numeros del menu.")    

