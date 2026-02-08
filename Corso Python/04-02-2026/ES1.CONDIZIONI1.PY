#Esercizio 1: 3 condizioni if annidate su 3 livelli di passaggio
domanda = input("giochi a pokemon" "(si/no)").lower() 
#.lower evita problemi di risposta con maiuscola
if domanda == "si":
    gen = int(input("quale generazione è la tua preferita? [1, 2, 3, 4, 5, 6, 7, 8, 9]")) 
    #int per trasformare risposta in numero
    if gen == 3:
        print("anche la mia!")
        starter = input("che starter hai preso tra treecko, torchic, mudkip ?").lower()
        if starter == "treecko":
            print("sei veramente un intenditore!")
        else: 
            #se if non è vera la risposta è la seguente
            print("carina come scelta!")
            
#Esercizio 2: creare if con elif vari e else finale che gestisca crud (aggiungi rimuovi elimina)
#CRUD - Create, Read, Update, Delete
dati = ["AM", "Taylor Swift"]

print(dati)
print("1 - Aggiungi")
print("2 - Rimuovi")
print("3 - Elimina tutto")

scelta = input("scegli un'opzione: ")

if scelta == "1":
    musica = input("scegli una band o cantante che ti piace: ")
    dati.append(musica)#aggiunge la scelta dell'utente in lista
    print(dati)
    
elif scelta == "2":
    rimuovi = input("scegli chi eliminare")
    dati.remove(rimuovi)#rimuove l'opzione scelta dall'utente
    print(dati)
    
elif scelta == "3":
    dati.clear()
    print("dati rimossi")
else:
    print("scelta non valida")
    
#Esercizio 3

    