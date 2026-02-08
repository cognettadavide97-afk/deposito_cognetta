"""Descrizione: Scrivi un programma che chieda all'utente di inserire due
numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 

Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
non valida"."""

print("--- CALCOLATRICE FAI DA TE ---")

#variabile che mi permette di ripetere le operazioni in un ciclo while
continua = "si"

while continua == "si":
    a = float(input("digita il primo numero: "))
    operazione = input("che tipo di operazione vuoi effettuare?" "(+, -, *, /)")
    b = float(input("digita il secondo numero: "))
    
    #match per distinguire le varie operazioni
    match operazione:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a*b)
        case "/":
            #if-else per impedire il crash su una divisione per zero
            if b != 0:
                print(a/b)
            else:
                print("impossibile dividere per zero!")
        #case _ per distinguere valori diversi dalle 4 operazioni assegnate
        case _:
            print("operazione non riconosciuta.")

    continua = input("vuoi eseguire una nuova operazione? (si/no)").lower()
