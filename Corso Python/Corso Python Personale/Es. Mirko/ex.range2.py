"""
ESERCIZI PYTHON: range()

1. Base / Numeri pari e dispari o sequenza
Descrizione:
Scrivi un programma che chiede all'utente di inserire un numero o una stringa 
scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o 
dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.

comando = input("Scegli un'opzione (numero / parola): ").lower()"""

"""while True:
    match comando:
        case "parola":
            scelta = str(input("Inserisci una parola: ")) #inizializzo l'input per far scrivere una stringa
            lunghezza = len(scelta) #"uso la funzione len per cocnvertirla in numero"
            print(f"La parola '{scelta}' è lunga {lunghezza} caratteri.")
            
            if lunghezza % 2 == 0: #verifico se è pari o dispari
                print("La lunghezza è pari.")
            else:
                print("La lunghezza è dispari.")
                
        case "numero": 
            n = int(input("Inserisci un numero: "))
            
            if n % 2 == 0:
                print(f"Il numero {n} è pari.")
            else:
                print(f"Il numero {n} è dispari.")
                
        case _:
            print("Opzione non valida.")
            
    scelta = input(print("vuoi continuare?: (si / no)")).lower
    if scelta != "si": 
        print("Arrivederci!")
        break
    else:
        continue"""

"""2. Intermedio / Numeri primi in un intervallo:
Chiedi all'utente di inserire due numeri che definiscono un intervallo (es. 10 e 50). 
Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo 
o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni 
differenti e chiedere se deve ripetere."""

print("prego, inserire due numeri interi in modo da definire un intervallo")
n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
lista_numeri = []

for i in range (n1-1, n2):
    print(lista_numeri.append(i), end=" ")
    len(lista_numeri)
    if lista_numeri(i) % 2 == 0:
        print("i seguenti numeri sono primi:", lista_numeri(i))
        lista_numeri.append(i)
        lista_primi = lista_numeri.append(i)
        print(lista_primi)
    else:
        print("i seguenti numeri non sono primi", lista_numeri(i))
        lista_numeri.append(i)
        lista_non_primi = lista_numeri.append(i)
        print(lista_non_primi)


"""3. Avanzato / Fattori comuni
Descrizione:
Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e 
stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni 
oltre 1, dovrebbe stampare "I numeri sono coprimi". 
La stessa cosa ma anche per due stringhe (.equal) e chiedere se deve ripetere 
ma sono "complementari" solo se hanno tutte le lettere in comune (es: abs/ sab)"""

print("prego, inserire due numeri interi in modo da definire un intervallo")
n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))
lista_numeri = []




        
    