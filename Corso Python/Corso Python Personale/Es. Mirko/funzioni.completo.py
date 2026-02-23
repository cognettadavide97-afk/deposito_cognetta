# 1. Chiedi all'utente di inserire un numero intero positivo n. 
# Se l'utente inserisce un numero negativo o zero, continua a chiedere 
# un numero fino a quando non viene inserito un numero positivo.
# 2. Genera una lista di numeri interi casuali tra 1 e n (incluso). 
# La lunghezza della lista deve essere n.
# 3. Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
# 4. Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.

# 5. Utilizza una funzione per determinare se un numero è primo. 
# La funzione deve restituire True se il numero è primo, altrimenti False.

# 6. Utilizza un ciclo for per stampare tutti i numeri primi nella lista.

# 7. Infine, utilizza una struttura if per determinare se la somma di tutti 
# i numeri nella lista è un numero primo e stampa il risultato.

import random #prendo il modulo random per generare casualmente la mia lista

while True: #creo un ciclo while per poter verificare che n è positivo.
    n = int(input("inserisci un intero positivo n: "))
    if n <= 0:
        print("per favore inserisci un intero positivo n: ") #avviso all'utente di inserire un n positivo. il ciclo si ripete
    else:
        break #break per procedere

lista_n = []
for i in range (n): 
    random_list = random.randint(1, n) #modulo randint per creare la lista. Stop ad n perché deve essere la lunghezza della lista
    lista_n.append(random_list) #utilizzo il modulo append per inserire il range in una lista
print(f"{lista_n}")

somma_pari = 0 #creo la variabile di partenza per i numeri 
for numero in lista_n:
    if numero % 2 == 0:
        somma_pari = numero + somma_pari
print(f"{somma_pari}")
        
for numero in lista_n:
    if numero % 2 != 0:
        print(numero, end=" ")

def prime(num):
    if num < 2:
        return False #poiché 0 e 1 non sono primi
    
    for i in range (2, num):
        if num % i == 0:
            return False
    return True

print("\n Numeri primi nella lista: ", end="")
for x in lista_n: # Uso x o un altro nome per non confondermi con n
    if prime(x):
        print(x, end=" ")
print()

somma_totale = sum(lista_n) 

if prime(somma_totale):
    print(f"La somma totale ({somma_totale}) è un numero primo!")
else:
    print(f"La somma totale ({somma_totale}) NON è un numero primo.")