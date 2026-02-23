"""chiedi all'utente di inserire un numero. il programma quindi dovrebbe fare un conto alla rovescia a partire da quel numero fino a 0
stampando ogni numero e chiederti se vuoi ripetere o nonlocal"""

n = int(input("inserisci un numero intero: ")) #n per inizializzare la variabile

for i in range(n, -1, -1):
    print(i)
    
#la voglio uniformare in un'unica riga quindi aggiungo il commando end= al print

n = int(input("inserisci un numero intero: ")) #n per inizializzare la variabile

for i in range(n, -1, -1):
    print(i, end=" ")

"""Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se il numero inserito è primo/pari o no. Se è primo lo salva 
e stampa "il numero è primo". Altrimenti stampa "il numero non è primo". Si ferma il tutto quando hai 5 numeri"""

numeri_salvati = []
conteggio = 0 #inizializzo il conteggio

while conteggio < 5:
    
    n = int(input("inserisci un numero intero: ")) #inizializzo la variabile internamente al ciclo while altrimenti non lo richiede
    conteggio += 1 #impongo che il conteggio aumenti ogni volta che trova un nuovo numero. Il conteggio sale di 1. stesso discordo di n
    numeri_salvati.append(n) #utilizzo il METODO integrato .append() per salvare i numeri in lista durante il ciclo

    
    if n % 2 == 0: #verifico se il numero inserito è primo o no
        print("Il numero è pari")
    
    else:
        print("il numero è dispari")
        
    if n < 2:
        print("Il numero è primo")
    else:
        n_primo = True #inizializzo una nuova variabile impostata su True. La condizione iniziale che è vero che sono n primi
        
    #ora verifico se la condizione iniziale è vera con un ciclo for, dove divido tutto per 2 e n-1
    for i in range(2, n):
        if n % i == 0:
            n_primo = False # Abbiamo trovato un divisore!
            break           # Inutile continuare a cercare
        
        if n_primo:
            print(f"{n} è primo")
        else:
            print(f"{n} non è primo")
    
        
print(numeri_salvati) #print fuori dal ciclo while cosi stampa tutto solo alla fine

        
    

"""Esercizio completo
Esercizio su Python: Cicli e Condizioni
Punto 1: Utilizzo di if
Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.
Punto 2: Utilizzo di while e range
Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da n a 0 (compreso), decrementando di 1. 
Deve potersi ripetere all'infinito.
Punto 3: Utilizzo di for
Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero nella lista.
Punto 4: Utilizzo di if, while e for insieme
Scrivi un sistema che prende in input una lista di numeri interi che precedentemente è stata valorizzata dall'utente. Il sistema deve:
Utilizzare un ciclo for per trovare il numero massimo nella lista.
Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista."""


lista_numeri = [] #creo una lista per il punto 4. Da riempire

n = int(input("inserisci un numero intero: "))
    
if n % 2 == 0:
    print("il numero è pari")
else: 
    print("il numero è dispari")

while True: #impongo un ciclo while con una condizione di True  per avere un ciclo infinito
    n = int(input("inserisci un numero intero: "))
    
    for i in range(n, -1, -1): #n è lo start del range, -1 è lo stop, ovvero lo 0, il secondo -1 invece è il contatore che scende
        print(i, end =" ")
        lista_numeri.append(i)
        
    print(lista_numeri)

    for i in lista_numeri:
        print(i**2)

    for p in lista_numeri:
        print(max(lista_numeri))
    
    while len(lista_numeri) > 0:
        print(len(lista_numeri))
        break
    
    print(lista_numeri)

    while len(lista_numeri) == 0:
        print("lista vuota")
        break