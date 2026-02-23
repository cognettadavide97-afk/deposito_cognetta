"""Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola."""

parole = ["caio", "semprogno", "tizio"]

def trasformazione_lista(lista): #la funzione trasforma una lista. cosa? una lista. Meglio scrivere lunghezza come nome funzione
    
    risultato = []
    
    if len(lista) != 0:
        for parola in lista:
            risultato.append(len(parola))
            
    return risultato

print(trasformazione_lista(parole))