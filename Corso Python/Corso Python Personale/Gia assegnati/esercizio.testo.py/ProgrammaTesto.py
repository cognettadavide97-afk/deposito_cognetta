"""Create un programma in 2 parti:
- prima parte genera 5 numeri
casuali e li salva su un file
- seconda parte, rilegge il file e
l’utente dovrà cercare di indovinarne almeno 2 di quei numeri 
oppure avrà perso."""

import random

numeri_casuali = [random.randint(1, 50) for _ in range(5)]

with open("numeri.txt", "w") as file:
    for numero in numeri_casuali:
        file.write(f"{numero}\n")

print("File creato e numeri salvati con successo!")



