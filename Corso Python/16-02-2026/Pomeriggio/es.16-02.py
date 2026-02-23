"""create un programma che richiede all’utente tre numeri e verifica la presenza di almeno due numeri uguali,
se non ci sono ci restituisce il numero più grande dei tre"""

a = int(input("inserisci un numero: "))
b = int(input("inserisci un secondo numero: "))
c = int(input("inserisci un terzo numero: "))

if a == b or c:
    print(a, "e", b or c, "sono uguali" )
elif b == c:
    print(b, "e", c, "sono uguali")
elif a > b and c:
    print(a, "è un numero maggiore degli altri")
elif b > a and c:
    print("b è un numero maggiore degli altri")
elif c > b and a:
    print(c, "è un numero maggiore degli altri")
else:
    print("errore")

#LOGICA CORRETTA
# Verifica se ci sono almeno due numeri uguali
if a == b or a == c or b == c:
    # Qui gestiamo i vari casi di uguaglianza
    if a == b:
        print(f"{a} e {b} sono uguali")
    elif a == c:
        print(f"{a} e {c} sono uguali")
    else:
        print(f"{b} e {c} sono uguali")

# Se non ci sono uguali, cerchiamo il maggiore
elif a > b and a > c:
    print(f"{a} è il numero maggiore")
elif b > a and b > c:
    print(f"{b} è il numero maggiore")
else:
    print(f"{c} è il numero maggiore")