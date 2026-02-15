#reto grande (8)
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
saldo_i = float(input("Ingresa tu saldo inicial: "))
if saldo_i < 0:
    print("ERROR")
else:
     pregunta = input("¿Quieres depositar?").lower()
     if pregunta == "si":
         deposito = float(input("Ingresa la cantidad a depositar :"))
         if deposito < 0:
             print("No puedes ingresar una cantidad NEGATIVA")
         else:
                 saldo_f = deposito + saldo_i
                 print("Tu saldo actual es de : " , saldo_f)
     else:
         saldo_f = saldo_i
     pregunta_2 = input("¿Quieres retirar?").lower()
     if pregunta_2 == "si":
         retiro = float(input("¿cuanto quieres retirar?"))
         if retiro < 0:
             print("No puedes ingresar una cantidad NEGATIVA")
         elif retiro > saldo_f:
             print("Saldo insuficiente")
         else:
             saldo_f = saldo_f - retiro
             print("Tu saldo actual es : ",saldo_f)
     if edad <= 12:
       print("Tienes un descuento del 50%")
     elif edad <= 17:
        print("Tienes un descuento del 30%")
     else:
        print("No tienes descuento")
     if saldo_f > 1000:
        nivel = "vip"
        print("VIP")
     elif saldo_f > 500:
         nivel = "Frecuente"
         print("Frecuente")
     else:
         nivel = "Basico"
         print("Basico")
     print("----Resumen del usuario----")
     print("----",nombre,"----")
     print("----",saldo_f,"----")
     print("----",nivel,"----")
     print("----",edad,"----")