x = 15
y = 18
if (x < y):
    print ("30 e lode")
    
x = 15
y = 18
if (x > y):
    print ("30 e lode")
else: #deve essere l'errore a if
    print ("ripeti la matematica")
    
x = 15
y = 18
if (x < y):
    print ("30 e lode")
elif (x == y): #condizione ausliara
    #diverso ma non in contrasto
    print ("bravo")
else:
    print ("ripeti la matematica")
    
numero = 10
if numero > 0:
    print ("il numero è positivo")
    if numero == 10: #condizione annidata
        print("waoh")
        
x = 15
y = 18
if (x + y == 33):
    print ("BRAVO")
    
comando = input("inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("chiusura del programma.")
    case "pausa":
        print("programma in pausa")
    case _:
        print("commando non riconosciuto.")