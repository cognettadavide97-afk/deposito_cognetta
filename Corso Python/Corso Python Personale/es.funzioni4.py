"""Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari."""

lista = []

while True:
    n = int(input("inserisci un numero intero: "))
    if n < 0:
        print("per favore inserisci un numero intero")
    else:
        domanda = input("vuoi stampare un altro numero?: si/no")
        if domanda == "no":
            break
        elif domanda == "si":
            continue
        else:
            print("per favore inserisci si o no")
    lista.append(n) 
"""Cosa succede qui?
Poiché lista.append(n) si trova alla fine di ogni giro del ciclo (fuori dal blocco else), 
il computer aggiungerà il numero alla lista anche se è negativo."""
            
def lista_pari(filtro_numeri): 
    
    nuova_lista = []
    
    for numero in filtro_numeri:
        if numero % 2 == 0:
            nuova_lista.append(numero)
        """Il break dice al computer: "Esci immediatamente dal ciclo!".
Messo lì, il computer controllerà il primo numero e, sia che sia pari sia che sia dispari, interromperà il giro. 
Quindi la funzione controllerà sempre e solo il primo elemento della lista."""
    return nuova_lista

print(lista_pari(lista))
        
        
"""ESERCIZIO CORRETTO

lista = []

while True:
    # 1. Prendiamo l'input e lo aggiungiamo SEMPRE alla lista
    n = int(input("inserisci un numero intero: "))
    lista.append(n) 
    
    domanda = input("vuoi inserire un altro numero? (si/no): ").strip().lower()
    if domanda == "no":
        break

def lista_pari(filtro_numeri):
    nuova_lista = []
    
    for numero in filtro_numeri: # 'numero' è l'elemento corrente
        if numero % 2 == 0:     # Controlliamo 'numero', non 'n'!
            nuova_lista.append(numero)
        # NESSUN break qui, altrimenti ci fermiamo al primo numero!
            
    return nuova_lista # Restituiamo tutto alla fine del ciclo

print("Numeri pari trovati:", lista_pari(lista))"""
