lista = [[]]
print(lista[3][1])
print(lista[-1][1])

lista = ["zero","uno","due","tre","quatro","cinque"]

#tutti gli elementi da 1 a 4
lista2 = lista[1:5] #se è il primissimo numero posso scrivere [:5] 
#o viceversa [1:]
print(lista2)

#[::-1] inverte la lista
#[1:5:2] start, end, passo
#lista.extend() mi "somma" le due liste
#lista.reverse() mette al contrario
#lista.index("oggetto")

var = "ciao a tutti"
print(var.startwith("ciao"))
var.endwith("tutti")

print(var.isalnum()) #sia per caratteri che numeri alpha num, no spazi
print(var.isalpha()) #numeri
var.isdecimal, var.isdigit #fanno conversione numerica 
#NOTA solo per i numeri interi perché "." è un char

lista = ["pippo", "franco", "ugo"]
nome1,nome2,nome3 = lista #dobbiamo inserire tutte le var
nome1,_,_, = lista #alternativa
print(nome1) #molto utile per un singolo el di una sola lista
#metodo separatore delle stringhe
sep = "-"
stringa = sep.join(lista)
print(stringa)

stringa = "ciao a tutti"
stringa2 = stringa[1:5] 
#print "iao"

print("ciao" in stringa) #verifica se l'elemento è nella stringa.
#restituisce True
#NOTA: per nelle liste gli el sono quelli sep dalla virgola
#nelle stringe gli el sono tutti gli el del carattere

"CICLO FOR"
#for dice prendi tutti gli elementi di una variabile e salvali
for char in stringa:
    print(char) #stampa tutti gli el della stringa
    
print(char) #ci trovi solo l'ultimo carattere perché l'ultimo el ciclato
#è un carattere (l'ultimo carattere della stringa)

print(list(range(3))) #range evita di farci scrivere un iterabile

"""while index"""

#LIST COMPRHENSION
"OPERATORE TERNARIO"
lista = [nome for nome in lista if "a" in nome]
#inserisci inserisci nome se nome è presente in lista e ha "a" nel nome

Cliente = {"nome": "teresa" "tommaso", "cognome": "rossi" "Muraca"}
clienti = {'1: cliente1'
           '2: cliente2'}

for key in clienti:
    print([key], "nome")
    
for key, valore in key.items(): #items restituisce un dato specifico dei dict, "dict_items"
    print(key, valore)
    
""".items
.key
.values"""

#metodo per cercare el in una lista senza error
print('clienti1'["indirizzo"])
#supero l'errore con .get(value)
#get ha 2 argomenti, uno che cerca e uno che restituisce solo se lo trova (es. nome, el non trovato)
# cosa fa .setdefault?

lista = ["tommaso", "teresa", "alfredo"]

for i, nome in enumerate(lista):
    print(f"indice{i}, nome:{nome}")
    
# .sort vs sorted() .sort è specifico delle liste

tupla = (5, 1, 12, 7, 3)

print(sorted(tupla))
print(sorted(tupla, reverese=True))

#utilizzo ulteriore di list comprehension
lista = [nome for nome in lista if "a" in nome]
print('lista3')

diz1 = {nome:nome+str(1) for nome in lista if "a" in nome}
print(diz1)

#FUNZIONI
def somma(a=0, b=0):
    print(a+b)
    
somma(15,5,10) #10 non identificato

#soluzione
def somma(*a):
    print(type(a))
    
somma(15,5,10)
#trasforma in tupla

def somma(**a):
    print(type(a))
    print(a["num1"] +1)
    
somma(num1=15,num2=5,num3=10)
#trasforma in dizionario

def funzMy():
    val = 15 #spazio memoria locale NON globale
    #serve return val
    
funzMy()
print('val') #non lo trova perché non posso richiamarlo

numeri = [1,2,3,4,5] #come modifico senza list comprehension?
#sol
numeri2 = []
for i in numeri:
    numeri2.append(i*3)
    print(numeri2)
    
#funzione per semplificare
def moltiplica(a):
    return a*3

for i in numeri:
    numeri2.append(moltiplica(i))
    
#funzione map
numeri = list(map(moltiplica, numeri)) #passa i singoli el di numeri
print(numeri)
#utile per gli iterabili che si vogliono convertire
#il risultato è lo stesso di un ciclo for

def pari(n):
    return n % 2 == 0
#restituisce false se il resto non è 0

#alternativa 2
lista_pari = []
for i in numeri:
    if not pari:
        numeri.removi(i)
print(numeri)

lista_pari = []
for i in numeri:
    if pari(i):
        numeri.append(i)
print(numeri)
        
#FILTER FUNZIONE (filtra gli el di un iterabile. Deve rest True o False)
#True = passa, False = non passa
numeri = list(filter(pari, numeri))

print(numeri)

#FUNZIONE LAMBDA
def DoppioNum(x):
    return x*x #utile come sol temporanea

lambda x:x*x #gli argomenti che accetta e poi l'operazione che fa.
#elaborazione su singola riga, può essere utile nel map o filter

#LAMBDA NEL MAP
numeri = [1,2,3,4,5]
numeri = list(map(lambda x:x*3, numeri)) #passa i singoli el di numeri
print(numeri)
#non salva in memoria. Utile per qualcosa che non ci servirà in futuro
#restituisce [3,6,9,12,15]

"LIBRERIE"
#esistono librerie già "preimpostate", come random
import random #ci permette di importare la libreria

from random import randit, choice #cosi impporto solo quello che voglio

lista = [2,4,1,35]

print(choice(lista)) #sceglie un val randomico

#creare un modulo con dentro le funzioni da poter importare
#chiami funzioni.py (o comunque riconoscibile)
#posso importarla come fosse una libreria
#in python non esiste il formato data. usiamo libreria "datetime"
#stessa cosa per "time" print (datetime.time(15,40,00))
#datetimedatetime ti da gg/mm/aa e ora/min/sec
#con .now ci restituisce quello attuale della nostra macchina
"""le librerie sono presenti nel python packaging index dove tutti
caricano le proprie librerie. Panda è importante e ha anche il 
proprio sito web
pip install pandas - per installarlo ci basta usare pip già
presente al momento dell'installazione di python"""
#pip list ci permette di vedere tutte le librerie presenti nel nostro sistema
#conda per gli end

"TRY IN PYTHON"
numero = input("inserisci un numero: ")

try:
    print(int(numero)+5)
except:
    print("numero non valido!")
print("eseguo il programma")

"""utile per robe tipo non dover verificare il contenuto in una stringa
snellisce di molto il codice perché diamo subito errore all'utente senza
far crashare il programma."""

"importante imparare a riconoscere gli errori per lavorare su errori specifici"
try:
    print(int(numero)+5)
except ValueError as e:
    print("numero non valido!", e)
print("eseguo il programma")
#è come un if-else

with open("nome del file", ""):
    pass

#r leggerlo, w sovvrascrivere, a appendere, x solo a creare il file

with open("nome del file", "r") as file:
    contenuto = file.read
#devo dargli un acronimo 

def leggifile():
    with open("nome del file", "r") as file:
        contenuto = file.read
        
#scrivere un file
def scrivifile():
    with open("file2.txt", "w") as file:
        file.write("ciao")
        
#con append se non c'è il file lo crea come w, se no aggiunge la stringa
#per trovare una posizione trasformo una stringa in lista di lista
cont = leggifile()
print(cont)
#utilizzo del for o readlines(), ci crea si una lista ma con il backslash
listaR = cont.split("\n")
matrice = [x.split(",") for x in listaR]
print(matrice)
#lsita di lista, cioè una matrice che contiene una lista per ogni riga
#come sostituisco l'elemento?

for riga in range(len(matrice)):
    if matrice[riga][1] == "rossi":
        matrice[riga][1] = "verdi"
        
stringaF = "\n".join(matrice)
print(stringaF)

"""se no sapessi dall'inizio dove si trovasse il nome dell'utente 
potevamo dare direttamente il comando"""

matrice[2][0] = "alfredo"

def scrivifile():
    with open("file2.txt", "w") as file:
        file.write("ciao")
scrivifile(stringaF)
#cosi modifichiamo il file. Se aggiorniamo compare anche qui