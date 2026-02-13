"""1. Esercizio Base: Indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). 
L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, 
il programma dovrebbe dire all'utente se il numero da indovinare è più alto o più basso rispetto al numero inserito. 
Il gioco termina quando l'utente indovina il numero o decide di uscire."""

#carico libreria di generatori numeri casuali
import random

def genera_numero():
    """Genera e restituisce un numero casuale tra 1 e 100."""
    return random.randint(1, 100)

def indovinello(numero_random, tentativo):
    if tentativo < numero_random:
        print("il numero è più alto")
        return False
    elif tentativo > numero_random:
        print("il numero è più basso")
        return False
    else:
        print("bravo hai indovinato")
        return True

#funzione principale che gestisce il gioco:
def gioco():
    numero_da_indovinare = genera_numero()
    indovinato = False
    tentativi = 0

    print("scegli un numero da 1 a 100")
    
    while not indovinato:
        try:
            proposta = int(input("inserisci il tuo tentativo: "))
            tentativi += 1
            indovinato = indovinello(proposta, numero_da_indovinare)
        except ValueError:
            print("inserisci un numero intero valido")

    print(f"hai vinto in {tentativi} tentativi")
    
gioco()