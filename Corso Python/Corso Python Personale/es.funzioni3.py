#Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.

parola_utente = []

while True:
    parola = input("inserisci una parola: ").strip().lower()
    parola_utente.append(parola)
    loop = input("vuoi inserire una nuova parola? (si/no)").strip().lower()
    if loop == "no":
        break
    elif loop != "si":
        print("errore! inserisci si o no")


def lista_parole(lista_da_filtrare):
    # 1. CREO IL SECONDO CESTO (VUOTO)
    risultato = [] 

    # 2. GUARDO OGNI PAROLA DELLA LISTA ORIGINALE
    for parola in lista_da_filtrare:
        # 3. CONTROLLO (SE la parola esiste E SE inizia con le lettere giuste)
        if parola and parola[0] in ["d", "a", "c"]:
            # 4. AGGIUNGO SOLO SE IL CONTROLLO È SUPERATO
            risultato.append(parola)
    
    # 5. SOLO DOPO CHE IL CICLO FOR È FINITO (fuori dal for), RESTITUISCO TUTTO
    return risultato

print(lista_parole(parola_utente)) #cosa succede? la funzione prende il procedimento per cui vengono filtrate le parole che iniziano con
#d, a, c. inserendo il valore effettivo, cioè parola utente, la funzione applicherà il processo sulle parole dentro parola_utente
