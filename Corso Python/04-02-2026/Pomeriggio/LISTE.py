numeri = [1, 2, 3, 4, 5] #lista di numeri
nomi = ["Alice", "Luca", "Marco"] #lista con stringhe
misto = [1, "Marco", True, 4.5, "due"] #lista di oggetti misti
liste = [numeri, nomi, misto] #lista di liste
print(liste)
print(liste[1])

numeri= [3, 1, 4, 2, 5]
print(len(numeri)) #output: 5
numeri.append(6)
print(numeri)
numeri.remove(4)
numeri.sort()
print(numeri)