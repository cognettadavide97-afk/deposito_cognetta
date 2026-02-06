def fibonacci(n):
    a, b = 0, 1
    
    while a < n:
        yield a
        a, b = b, a + b
        
# Devi chiamare la funzione e dirgli cosa fare con i numeri prodotti
for numero in fibonacci(100):
    print(numero)    
    
import random
def generatore_casuale(minimo, massimo):
    """Genera numeri casuali all'infinito tra minimo e massimo."""
    while True:
        yield random.randint(minimo, massimo)
# --- ESEMPIO DI UTILIZZO ---
# Inizializziamo il generatore tra 1 e 100
numeri_random = generatore_casuale(1, 100)
# Stampiamo i primi 5 numeri generati
print("Ecco i tuoi numeri fortunati:")
for _ in range(5):
    print(next(numeri_random))
#-------------------------------------------------------------------------
moltiplicatore = int(input("inserisci un numero"))
def quadrato(c, lim):
    
    while c % 2 == 0 and c < lim:
        yield c
        c = c*moltiplicatore

for numero in quadrato(2, 1000):
    print(numero)
    
# Chiediamo all'utente la base della moltiplicazione
moltiplicatore = int(input("Inserisci il moltiplicatore: "))

def quadrato(c, limite_valore, passo):
    # Passiamo 'passo' come argomento così la funzione sa per cosa moltiplicare
    while c % 2 == 0 and c < limite_valore:
        yield c
        c = c * passo 

# 1. Chiediamo l'input
moltiplicatore_utente = int(input("Inserisci il moltiplicatore: "))

# 2. Chiamiamo la funzione passando TUTTI i dati necessari
for numero in quadrato(2, 1000, moltiplicatore_utente):
    print(numero)
    
    