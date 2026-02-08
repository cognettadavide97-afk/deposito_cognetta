"""chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se il numero inserito
è primo / pari o no. Se è primo, lo salva e stampa "il numero è primo." Altrimenti, stampa "il numero non è primo"
si ferma il tutto quando ha 5 numeri primi"""

numero = int(input("inserisci un numero intero: "))

while True:
    if numero % 2 == 0:
        print("il nnumero è pari")
    elif numero

    else:
        print("il numero non è primo")