from random import randint

lista = []

def numeri_random(numero):
    for numero in range(5):
        numero = randint(1, 10)
        lista.append(numero)
    return numeri_random

with open("numeri2.txt", "w"):
    print(numeri_random(lista))