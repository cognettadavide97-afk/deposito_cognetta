#Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.

numeri = [2, 3, 4, 5]

def val_max(lista_numeri):
    if len(lista_numeri) != 0:
        max(lista_numeri) #non necessario si poteva direttamente scrivere return max(lista_numeri)
    return max(lista_numeri)
"""return None poteva essere inserito spostando l'indice di return max per avere anche una soluzione se la lista fosse stata vuota"""

print(val_max(numeri))