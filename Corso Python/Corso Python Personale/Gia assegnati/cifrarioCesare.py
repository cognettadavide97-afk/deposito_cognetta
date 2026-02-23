"""Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave."""

def cifrario_cesare():
    # 1. Definiamo l'alfabeto in una lista
    alfabeto = list("abcdefghijklmnopqrstuvwxyz")
    
    # 2. Input dall'utente
    print("--- Cifrario di Cesare ---")
    messaggio = input("Inserisci la parola: ").lower()
    chiave = int(input("Inserisci il valore della chiave (numero): "))
    modalita = input("Vuoi (C)riptare o (D)ecriptare? ").upper()

    # Se l'utente vuole decriptare, invertiamo il segno della chiave
    if modalita == 'D':
        chiave = -chiave

    # 3. Logica Lambda
    # La lambda prende l'indice della lettera attuale, somma la chiave 
    # e usa l'operatore modulo (%) per ricominciare da capo se supera la 'z'
    trasforma = lambda char: alfabeto[(alfabeto.index(char) + chiave) % 26] if char in alfabeto else char

    # 4. Applichiamo la lambda a ogni carattere della parola
    risultato = "".join(map(trasforma, messaggio))

    print(f"\nRisultato finale: {risultato.upper()}")

# Esecuzione del programma
cifrario_cesare()

