# Presentacion del sistema de validacion de productos
print("-------Sistema de compras-------")
print("    ")

print("Bienvenidos al portal interactivo")

# Le doy un a "nombre_producto" el cual es un imput de tipo str 
nombre_producto = input("Nombre del producto: ")
 
 # Instrucciones basicas de como debe ser utilizado que se visualizan en consolo
print("Recuerda que debe ser en numeros enteros")
print("el valor debe ser digitado en cifras de mil")
print("    ")

# Utilice un bucle "While" para que la estructura de control "try" acepte solamente valores numericos sin importar si son numeros enteros o reales
while True:
    try:
        valor_producto = float(input("Cual es el valor del producto: $"))
        break
    except:
        # Si el valor solicitado es de tipo "str" va a mandar el mensaje de precio valido hasta que se coloque un numero entero o real
        print("Precio no valido")

# Utilice otro bucle llamado "while" donde le asigno el valor a la variable de cantidad_producto que mostrara la pregunta con la cantidad de productos
# y solo se podra ingresar datos numericos enteros debido al "try" que tomo dentro del bucle "while"
while True:
    try:        
        candidad_producto = int(input("¿Cual es la cantidad de productos?: #"))
        break
# El "except" es para que en caso tal el usuario ingrese un valor que no es un numero entero muestra el mensaje de "Recuerda que son numeros enteros."
# y se repetira el bucle hasta que se registre un numero entero 
    except:
        print("Recuerda que son numeros enteros." )

# Le doy un valor a la variable "costo_total" que va a se igual a la cantidad del producto * el valor de producto
costo_total = valor_producto*candidad_producto

# Para mostrar el costo total del carrito
print("El costo total del carrito es de: ", costo_total)

# Le doy un valor a la variable "pregunta_descuento" el cual mostrara la prgunta si desa aplicar un descuento, ademas tiene la funcion ".upper" para que en
# caso tal el usuario coloque "Si" o "No" en mayuscula o miniscula la condicion "if" que esta abajo lo lea 
pregunta_descuento = input("¿Le desea aplicar descuento? (SI o NO): ").upper()

# Uso una condicional para explicar los casos posibles
# Si la variable pregunta descuento es igual "SI"
if pregunta_descuento == "SI":
    # El bucle "While" para que se repita 
    while True:
        #La estructura de control "try" para probar la entrada de datos
        try:  
            # Creo y le asigno un valor a la variable "descuento_producto" en donde la respuesta que espera del usuario sea en numeros enteros o numeros reales
            descuento_producto = float(input("¿Cual es el valor del descuento?: "))
            
            # La condicion "if" para determinar si la variable "descuento_producto" sea mayor que uno y menor que 100
            if descuento_producto >= 1 and  descuento_producto <= 100:
                
                # Creo la variable "descuento_realizado" y el valor que le doy es la variable "costo_total"*(descuento_producto/100) para tener certeza del valor exacto del descuento
                descuento_realizado = costo_total * (descuento_producto/100)
                
                # Creo la variable "descuento_aplicado" y el valor que le doy es la variable "costo_total" - "descuento_realizado" para tener certeza del valor exacto del total menos el descuento
                descuento_aplicado = costo_total - descuento_realizado
                
                # Utilizo "print" agrego el texto discriminando el descuento realizado concatenando la variable de "descuento_realizado" y tambien agrego el precio a pagar y concatenando la variable "descuento_aplicado"
                print(f"Su descuento realizado es: $ {descuento_realizado:.2f} y su precio a pagar es: $ {descuento_aplicado:.2f}")
                
                #Para darle fin al ciclo y continue con el resto
                break
            
            # En caso de que se ingrese algo totalmente distinto muestre al usuario "Opcion no valida."
        except:
            print("Opcion no valida.")
            
     # En caso donde el usuario en la variable "pregunta_descuento" escriba la opcion de "NO" muestre el mensaje de "No tienes descuento y tu valor total es:" con la concatenacion de la variable "costo_total"          
elif pregunta_descuento== 'NO':
    print(f"No tienes descuento y tu valor total es: {costo_total:.2f}")
    
    # En caso de que se marque algo totalmente distinto le de la respuesta de "Opcion no valida."
else:
    print("Opcion no valida.")

# Hecho para mostrarse al finalizar toda la validacion de compras
print("Gracias por su compra, esperamos que vuelva pronto")

    
    
    










