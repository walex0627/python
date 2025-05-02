#Ejercicios de condicionales
# 1. Dterminar signo y paridad
# Realizado por mi
"""
number = int(input("Please, enter a number: "))
mod = number % 2
while number > 0 :
    if mod > 0:
        print("You picked an positive odd number.")
    else :
        print("You picked an positive even number")


while number < 0:
    if number % 2 == 0 and number < 0:
     print("You picked an negative odd number.")
     break
    elif number < 0 :
        print("You picked an negative odd number.")
        break    
       
    """
    
# De una manera mas eficiente
"""while True:
    try:
        number = int(input("Please, enter a number: "))
        break
    except ValueError:
        print("Only a numerics value!")

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "cero"
    
if number % 2 == 0 :
    parity = "even"
else:
    parity = "odd"
    
print(f"Your number is {sign} and {parity}")"""

#2 Una persona ingresa su edad. Clasifica esa edad en una de las siguientes categorías:
 
"""edad = int(input("How are years old?: "))

if edad < 18:
    print("You're a minor")
elif edad >= 18 and edad <= 30:
    print("You're a young adult")
elif edad >= 31 and edad <= 65:
    print("You're a mature adult")
elif edad >= 65:
    print("You're a older adult")
else:
    print("Please enter a correct value")"""

#3 Tarifa de transporte según día y hora
"""while True:
    work_day = input("Is today a working day? (Normal/Work/Weekend): ").upper()
    if work_day in ["WORK", "WEEKEND", "NORMAL"]:
        break
    else:
        print("Enter a valid option")

day_hour = int(input("What time is it?: "))
value_ticket = 3300
work_taxes = 300
weekend_taxes= 200

if work_day == "WORK" and (7 <= day_hour <= 9) or (17 <= day_hour <= 19):
    peak_value = value_ticket + work_taxes
    print(f"The taxes of your ticket is {work_taxes} and your ticket cost {peak_value}") 
elif work_day == "WEEKEND":
    weekend_value = value_ticket + weekend_taxes 
    print(f"The taxes of your ticket is {weekend_taxes} and your ticket cost {weekend_value}")       
else:
    print(f"Your ticket dont have a taxes and the cost is {value_ticket}")
    """
    
#4 Descuento en tienda según monto y tipo de cliente

"""type_client = input("Are you a VIP client? (Y/N): ").upper()
amount = int(input("What is your amount?: "))


while type_client == "Y":
    if amount >= 500 and amount >= 0:
        percentage_vip_1 = 20
        discount_vip_1 = amount* (percentage_vip_1/100)
        final_price_1 = amount - discount_vip_1        
        print(f"Your discount is {discount_vip_1} and your final price is {final_price_1}")
        break
    elif amount <= 500 and amount >= 0:
        percentage_vip_2 = 10
        discount_vip_2 = amount* (percentage_vip_2/100)
        final_price_2 = amount - discount_vip_2       
        print(f"Your discount is {discount_vip_2} and your final pric is {final_price_2}")
        break
    else: 
        print("Enter a valid option.")
        
while type_client == "N":
    if amount >= 500 and amount >= 0:
        percentage_1 = 5
        discount_3 = amount* (percentage_1/100)
        final_price_3 = amount - discount_3        
        print(f"Your discount is {discount_3} and your final price is {final_price_3}")
        break
    elif amount <= 500 and amount >= 0:
        print(f"Your amount don't have a discount, your final price is {amount}")
        break
    else: 
        print("Enter a valid option.")
        """
        
        
    