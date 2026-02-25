"""Consegna:
Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta 
(cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, 
la matrice invertita, la diagonale principale e la matrice invertita modificata.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, 
modificare e manipolare sotto-matrici e array, applicando 
operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi."""

import numpy as np

arr2D = np.random.randint(1,100, size=(6, 6))
print(arr2D)

sotto_matrice4x4 = arr2D.copy()
print(sotto_matrice4x4[1:5, 1:5])

matrice4x4_invertita = sotto_matrice4x4[::-1, :].copy()
print(matrice4x4_invertita)

diag_matr_inv = sotto_matrice4x4.diagonal(offset=0, axis1=0, axis2=1).copy()
diag_matr_inv.flatten
print(diag_matr_inv)

matrix_change = matrice4x4_invertita[matrice4x4_invertita == 3]