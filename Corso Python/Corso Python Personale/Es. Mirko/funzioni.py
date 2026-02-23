"""
Def

1. Esercizio Base: Indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale 
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è 
stato generato. Dopo ogni tentativo, il programma dovrebbe 
dire all'utente se il numero da indovinare è più alto o più 
basso rispetto al numero inserito. Il gioco termina quando 
l'utente indovina il numero o decide di uscire."""

import random

n_segreto = random.randint(1, 100)

while True:
    risposta = int(input("scegli un numero tra 1 e 100 per indovinare: "))
    if risposta == n_segreto:
        print("bravo! hai indovinato")
        break
    elif risposta < n_segreto:
        print("sbagliato! prova più in grande!")
    elif risposta > n_segreto:
        print("sbagliato! vola in basso!")
    else:
        print("sbagliato! prova di nuovo")
        

"""2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il 
programma dovrebbe stampare la sequenza di Fibonacci fino a N. 
Ad esempio, se l'utente inserisce 100, il programma dovrebbe 
stampare tutti i numeri della sequenza di Fibonacci minori o 
uguali a 100.
"""

x=int(input("inserisci un numero intero: "))

a = 0
b = 1

while a + b <= x:
    a, b = b, a + b
    print(a, end=" ")
        
