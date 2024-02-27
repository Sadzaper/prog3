import random
print("===================================")
print("Welcome to the game of adivinanzas")
print("===================================")

numero_secreto = random.randrange(1,101)

print("Seleccione el nivel de dificultad")
print("(1)Facil  (2)Medio   (3)Dificl")
nivel = int(input("ingrese el nivel de dificultad: "))

if(nivel==1):
  total_intentos=3
elif(nivel==2):
  total_intentos=2
else:
  total_intentos=1

for iteracion in range(1,total_intentos+1):
   print("Intento: {} de {}".format(iteracion,total_intentos))
   entrada=int (input("Digite un numero"))

   print("Digitaste . . .", entrada)
   if(entrada<1 or entrada>100):
    print("Ingresar un numero entre 1 y 100")
   continue

   acertaste = entrada ==numero_secreto #iguales
   mayor = entrada >numero_secreto#mayor
   menor = entrada <numero_secreto#menor


   if(acertaste):
    print("Felicidiades!!. . . adivinaste el numero")
    break
   elif(mayor):
    print("Lo siento el numero que ingresaste es mayor que el numero secreto")
   else:
    print("lo siento elnumero que ingresdaste es menor que el numero secreto")

   iteracion = iteracion+1

print("Fin del juego")