"""Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) 
e la forma (shape) dell'array.

Esercizio:
    Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
    Verifica il tipo di dato dell'array e stampa il risultato.
    Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
    Stampa la forma dell'array."""
    
import numpy as np

arr = np.arange(10, 50)
print("dtype iniziale", arr.dtype)
print(arr)
print(arr.shape)
arr2 = np.arange(10,50).astype("float64")
print(arr2)
print("nuovo dtype", arr2.dtype)
