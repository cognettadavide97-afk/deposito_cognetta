x = int(input("Inserisci un numero: "))

if x > 0:
    print("È positivo")
    
    if x > 9:
        print("È un numero a due cifre o più")
        
        if x == 24:
            print("È il numero corretto")
        else:
            print("Non è il numero corretto")
else:
    print("È zero o negativo")

            
#esercizio 2
dati = []


#esercizio 1 - Match
#scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 anni, il programma dovrebbe stampare
#"mi dispiace, non puoi vedere questo film"
#altrimenti dovrebbe stampare "puoi vedere questo film"

eta = int(input("Inserisci la tua età: "))

match eta:
    case _:
        if eta < 18:
            print("Mi dispiace, non puoi vedere questo film")
        else:
            print("Puoi vedere questo film")

