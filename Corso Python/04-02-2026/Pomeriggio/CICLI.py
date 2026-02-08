conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio += 1
    
conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio += 2 #logica di rottura, senza questa parte di codice il while va in loop

controllore = True
#ciclo booleano
while controllore:
    print ("oh no")
    
    esci = input("vuoi uscire- SI - NO") #logica di rottura, senza ciclo infinito
    if esci.lower() == "si":#permette all'utente di controllare la domanda
        controllore = False #senza questo, controllore sempre vero
    else:
        controllore = True
        
numeri = [2, 1, 3, 4, 5]

for numero in numeri:
    print(numero)
    
nome = "davide"
for I in nome: #I è un placeholder per far partire il comando. Vale qualsiasi cosa
    print(I) #va messo anche in print
    #a lavoro su usa il tipo, es uso i numeri scrivo numeri. Uso parole, scrivo parole

for i in range(5):
    print(i)
    
for i in range(5, 21):
    print(i)
    
limite = int(input("scegli il limite massimo da raggiungere"))
for limite in range (23):
    print(limite)
