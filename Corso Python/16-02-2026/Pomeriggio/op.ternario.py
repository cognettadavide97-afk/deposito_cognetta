"""Scrivete un programma che chiede all'utente una
serie di parole e restituisce solo le vocali
e l’indice della vocale all’interno delle parole"""

lista_parole = []

while True:
    parola = input("scrivi una parola: ")
    lista_parole.append(parola)
    risposta = input("vuoi inserire un'altra parola? (si/no):").lower().strip()
    if risposta == "si":
        continue
    else:
        break

nuova_lista = [parole for parole in lista_parole if "d" in parole]
print(nuova_lista)

"""print("-" * 30)

# --- SVOLGIMENTO TRACCIA: Estrazione vocali e indici ---
for parola in lista_parole:
    print(f"Parola: {parola}")
    
    # Usiamo enumerate per avere sia la posizione (indice) che la lettera
    for indice, lettera in enumerate(parola):
        if lettera in vocali:
            print(f"  > Trovata vocale '{lettera}' all'indice {indice}")"""