"""chiedi all'utente di inserire un numero. il programma dovrebbe quindi fare un conto alla rovescia a partire 
da quel numero fino a zero, stampando ogni numero e chiederti se vuoi ripetere no."""

print ("--- CONTO ALLA ROVESCIA! ---")

while True:
    numero = int(input("inserisci un numero: "))
    for i in range(numero, -1, -1):
        print(i)
    
    continua = input("vuoi continuare? (si/no").lower()
    if continua == "si":
        print("ok!")
    elif continua not in ["si", "no"]:
        print("comando non riconosciuto")
        break
    else:
        break

