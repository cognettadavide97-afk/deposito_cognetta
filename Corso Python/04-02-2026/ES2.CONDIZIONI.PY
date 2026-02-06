#esercizio 1
eta = (input("sei maggiorenne?" "(si/no)"))
if eta == "si":
    print("puoi guardare questo film")
else:
    print("non puoi guardare questo film")
    
#esercizio 2
numero1 = float(input("inserisci un numero: "))
numero2 = float(input("inserisci un numero: "))
#float per permettere operazioni con decimali
operatore = (input("che tipo di operazione vuoi fare?" "[somma, differenza, moltiplicazione, divisione]"))
#utilizzo lista per maggiore correttezza
if operatore == "somma":
    print(numero1 + numero2)
elif operatore == "differenza":
    print(numero1 - numero2)
elif operatore == "moltiplicazione":
    print(numero1 * numero2)
elif operatore == "divisione":
    if numero2 == 0: #specifica della divisione per zero
        print("errore: divisione per zero")
    else: print(numero1 / numero2)
else: #chiusura del blocco if-elif-else
    print("operazione non valida")
            
#esercizio 2 prof (utilizzo match)
num1 = int(input("Inserisci primo numero: "))
num2 = int(input("Inserisci secondo numero: "))
operazione = input("Inserisci operazione (+ - * /): ")

match operazione:
    case "+":
        risultato = num1 + num2
        print(risultato)

    case "-":
        risultato = num1 - num2
        print(risultato)

    case "*":
        risultato = num1 * num2
        print(risultato)

    case "/":
        if num2 == 0:
            print("Errore: Divisione per zero")
        else:
            risultato = num1 / num2
            print(risultato)

    case _:
        print("Operazione non valida")