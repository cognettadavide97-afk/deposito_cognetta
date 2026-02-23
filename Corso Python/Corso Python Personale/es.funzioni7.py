"""Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga."""

parole = ["tizio", "caio", "semprogno"]

def max_parola(lista_parole):
    if len(lista_parole) != 0:
        return max(lista_parole)
    return None

print(max_parola(parole))

"""la funzione max() applicata alle stringhe non cerca la più lunga, ma quella che viene per ultima in ordine alfabetico.
Puoi dire alla funzione max quale criterio usare per il confronto. Usando key=len, gli dici: "Trova il massimo basandoti sulla lunghezza"""

#SOLUZIONE
def max_parola(lista_parole):
    if not lista_parole:
        return None
    
    parola_piu_lunga = lista_parole[0] # Iniziamo dalla prima
    
    for p in lista_parole:
        # Confrontiamo le lunghezze!
        if len(p) > len(parola_piu_lunga):
            parola_piu_lunga = p
            
    return parola_piu_lunga

