#Scrivi un programma che esegua le seguenti operazioni:
#Chiedi all'utente di inserire un numero intero positivo n. 
#Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero fino a quando non viene inserito un numero positivo.
#Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
#Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
#Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
#Utilizza una funzione per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
#Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
#Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato

num = int(input("Inserisci un numero intero positivo: "))
# Chiediamo il numero finché l'input è minore o uguale a zero
while num <= 0:
    num = int(input("Errore! Per favore inserisci un numero intero positivo: "))
# Creiamo un oggetto temporaneo per prendere il suo ID (indirizzo di memoria)
# e usiamo l'operatore modulo per portarlo nel range desiderato
n = 10
lista_casuale = []
for i in range(n):
    # id(object) restituisce un numero intero molto grande e variabile
    pseudo_random = (id(object()) + i) % n + 1
    lista_casuale.append(pseudo_random)
print(lista_casuale)

# 3. Calcola e stampa la somma dei numeri pari
somma_pari = 0
for x in lista_casuale:
    if x % 2 == 0:
        somma_pari += x

print("Somma dei numeri pari", somma_pari)
# 4. Stampa tutti i numeri dispari
print("Numeri dispari nella lista:", end=" ")
for x in lista_casuale:
    if x % 2 != 0:
        print(x, end=" ")
print() # Va a capo
# 5. Funzione per determinare se un numero è primo
def is_primo(n):
    # 1. I numeri minori di 2 (0, 1 e negativi) non sono primi
    if n < 2:
        return False
    # 2. Proviamo a dividere n per ogni numero (i) tra 2 e n-1
    for i in range(2, n):
        if n % i == 0:
            # Se il resto è 0, abbiamo trovato un divisore!
            # Quindi non è primo, restituiamo False e usciamo subito
            return False
 # 3. Se il ciclo finisce e non abbiamo mai trovato un divisore
    return True

# 6. Stampa tutti i numeri primi nella lista
print("Numeri primi nella lista:", end=" ")
for x in lista_casuale:
    if is_primo(x):
        print(x, end=" ")
print()

# 7. Verifica se la somma totale della lista è un numero primo
somma_totale = sum(lista_casuale)
print("Somma totale della lista", somma_totale)
if is_primo(somma_totale):
    print("La somma totale è un numero primo!")
else:
    print("La somma totale NON è un numero primo.")
     