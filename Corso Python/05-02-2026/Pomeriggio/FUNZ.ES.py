import random

def genera_numero():
    """Genera e restituisce un numero casuale tra 1 e 100."""
    return random.randint(1, 100)

def controlla_tentativo(segreto, inserito):
    """Confronta i due numeri e fornisce un suggerimento."""
    if inserito < segreto:
        print("Troppo basso! Prova un numero più alto.")
        return False
    elif inserito > segreto:
        print("Troppo alto! Prova un numero più basso.")
        return False
    else:
        print(f"Complimenti! Hai indovinato, il numero era {segreto}.")
        return True

def gioca():
    """Funzione principale che gestisce il ciclo del gioco."""
    numero_da_indovinare = genera_numero()
    indovinato = False
    tentativi = 0

    print("Benvenuto! Ho pensato a un numero tra 1 e 100. Prova a indovinarlo!")

    while not indovinato:
        try:
            proposta = int(input("Inserisci il tuo tentativo: "))
            tentativi += 1
            indovinato = controlla_tentativo(numero_da_indovinare, proposta)
        except ValueError:
            print("Per favore, inserisci un numero intero valido!")

    print(f"Hai vinto in {tentativi} tentativi!")

# Avvia il gioco
if __name__ == "__main__":
    gioca()