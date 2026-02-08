#17.Esercizio 1:  Condizioni e cicli
#Chieda all’utente di inserire un numero intero positivo. 
#Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
#Per ogni numero: stampi "pari" se il numero è pari 
#stampi "dispari" se il numero è dispari 
#Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.

n = int(input("Inserisci un intero positivo: "))

listarange = [] 
listap = []
listad = []

# Ciclo di validazione: impedisce al programma di proseguire finché n non è corretto
while n <= 0:
    print("Errore. Inserisci un intero positivo.")
    n = int(input("Inserisci un intero positivo: "))

# Il blocco seguente è fuori dal while: viene eseguito solo quando n > 0
# Elaborazione dei dati: popolamento delle liste tramite iterazione
for i in range(1, n + 1):
    listarange.append(i)
    # Smistamento dei valori in base alla divisibilità per 2
    if i % 2 == 0:
        listap.append(i)
    else:
        listad.append(i)

# Output dei risultati aggregati
print(listarange)
print(listad, "sono dispari")
print(listap, "sono pari")

# NOTA: 
# Non serve 'else' dopo il 'while' perché Python esegue il codice 
# sottostante in modo sequenziale non appena la condizione del ciclo fallisce.
    