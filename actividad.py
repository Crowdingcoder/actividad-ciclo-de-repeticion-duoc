import os
os.system("cls")

#actividad 1

print("actividad 1\n")

for x in range(1,11,1):
    print(f"numero: {x}")

#actividad 2

print("\nactividad 2:\n")
for x in range(2,21,2):
    print(f"Numerio:{x}")

#actividad 3

print("\nActividad 3:\n")

num = int(input("Ingrese un numero:\n"))
for x in range(1,11):
    multi = num * x
    print(f"{num} x {x} = {multi}")

#actividad 4

print("\nActividad 4:\n")
suma = 0
for x in range(1,101): #literal aqui es el orden de la operacion para que me salga bonito la operacion matematica
    total = suma + x
    print(f"{suma} + {x} = {total}")
    suma = suma + x
    
#actividad 5 

print("\nActividad 5:\n")
contador = 11
while contador > 0:
    contador = contador - 1
    print (f"Cuenta regresiva:{contador}")


#actividad 6

print("\nActividad 6:\n")
clave = "python123"
contraseña = input("Ingrese contraseña:\n")
while contraseña != clave:
    contraseña = input("Contraseña equivocada.\nIngrese contraseña:\n")
print("Contraseña aceptada.")

#actividad 7

print("\nActividad 7:\n")
n = int(input("Ingrese un numero:\n"))
print(f"numeros impares desde 1 al {n}:")
for x in range(1,n):
    if x % 2 != 0:
        print(x)
    
#actividad 8

print("\nActividad 8:\n")
numero = 69
adivinar = int(input("Ingrese un numero para adivinar:\n"))
while adivinar != numero:
    print("El numero ingresado no es el correcto.")
    if adivinar > numero:
        print("Te dare una pista, el numero a divinar es menor.")
    elif adivinar <numero:
        print("Te dare una pista, el numero a adivinar es mayor.")
    adivinar = int(input("Ingrese un numero para adivinar:\n"))
print("Acertaste felicidades")