import random

listaLetras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
numeroLetras = int(input("Introduce el número de letras: "))
contraseña = ""
for i in range(numeroLetras):
    letra = random.choice(listaLetras)
    contraseña = contraseña + letra
print(contraseña)
