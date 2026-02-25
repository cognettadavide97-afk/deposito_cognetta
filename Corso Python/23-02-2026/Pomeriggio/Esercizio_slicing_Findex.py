"""Consegna:
Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) 
assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre 
e modificare sottoarray specifici da un array più grande."""

from random import randint
import numpy as np

arr1D = np.random.randint(10,51, size=20)
print("Array completo:")
print(arr1D)


print("primi 10 el dell'Array:")
print(arr1D[:10])
print("ultimi 5 el dell'Array:")
print(arr1D[-5:])
print("el dal 5 al 15 dell'Array")
print(arr1D[5:15])
print("el dell'Array al passo 3")
print(arr1D[::3])

arr1D_edit = arr1D.copy()
arr1D_edit[5:10] = 99
print("Array modificato con val 99 da i 5 a i 10")
print(arr1D_edit)


