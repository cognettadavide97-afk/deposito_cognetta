import random
#prendo un comando in modo casuale
def pausa_caffè():
    bevande = ["caffè","cappuccino","espresso"]
    aggettivi = ["bollente","freddo","delizioso","cremoso"]
#dopo la funzione, necessario rientro (identazione)

    random_bevanda = random.choice(bevande)
#metto il valore "bevande" in modo casuale
#quando faccio partire il codice
    random_aggettivo = random.choice(aggettivi)

    messaggio = f"prenditi una pausa caffè {random_aggettivo} {random_bevanda}"
    return messaggio
#necessario "f" richiama la funzione?
#aggettivo e bevanda invertito
#cos'è return?
print(pausa_caffè())