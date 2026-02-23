"""Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi."""

lista_range = []

for i in range(0,10):
    print(i, end=" ")
    lista_range.append(i)

def somma_lista(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

print("\n somma", somma_lista(lista_range))