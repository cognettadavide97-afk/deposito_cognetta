import numpy as np

"""# Creazione di un array semplice
vettore = np.array([10, 20, 30])

print("Array NumPy:", vettore)
print("Tipo di dato:", type(vettore))

#creazione di un array unidimensionale. 1 riga 5 colonne
arr = np.array([1, 2, 3, 4, 5])
print (arr)

#creazione di un array bidimensionale. 2 righe 3 colonne
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)"""

# Creazione di un array

arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)  # Output: (5,)

print("Dimensioni dell'array:", arr.ndim)  # Output: 1

print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size)  # Output: 5

print("Somma degli elementi:", arr.sum())  # Output: 15

print("Media degli elementi:", arr.mean())  # Output: 3.0

print("Valore massimo:", arr.max())  # Output: 5

print("Indice del valore massimo:", arr.argmax())  # Output: 4

arr = np.arange(10)
print(arr) #Output: [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr) 
#Output: [[0 1 2] 
#        [3 4 5]]

