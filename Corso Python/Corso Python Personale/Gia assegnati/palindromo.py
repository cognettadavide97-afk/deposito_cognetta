"""Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma"""

print("--- PALINDROMO O NON PALINDROMO? ---")

def palindromo(testo):
    # 1. Pulizia: solo caratteri alfanumerici e tutto in minuscolo
    "ESPRESSIONE GENERATRICE"
    testo_pulito = "".join(c.lower() for c in testo if c.isalnum())
    
    # 2. Inversione della stringa
    testo_invertito = testo_pulito[::-1]
    
    print(f"hai scritto {testo_pulito}")
    print(f"al contrario si legge {testo_invertito}")
    
    return testo_pulito == testo_invertito

testo = input("inserisci una parola o frase: ")

if palindromo(testo):
    print("la parola o frase è palindroma")
else:
    print("la parola o frase non è palindroma")
    


"""
testo = input("inserisci una parola o frase: ")
testo_edit = "".join(carattere for carattere in testo if carattere.isalnum())
lista.append(testo_edit)
testo_invertito = testo_edit[::-1]"""

