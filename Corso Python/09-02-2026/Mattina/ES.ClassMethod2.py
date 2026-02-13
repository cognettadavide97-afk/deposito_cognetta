"""devo creare una biblioteca con python che permetta all'utente di creare un libro e stamparlo"""

class Libro:
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def stampa_libro(self, libro:Libro):
        print(f"Libro: {self.titolo}, autore: {self.autore}, pagine: {self.pagine}")
        
class Biblioteca:
    def __init__(self):
        self.catalogo = ()
        
    def libreria(self, libro_da_inserire):
        self.catalogo.append(libro_da_inserire)
        print(f"Hai inserito {libro_da_inserire.titolo} ")

#faccio inserire all'utente le variabili
titolo_utente = input("inserisci il titolo del libro: ")
nome_autore = input("inserisci il nome dell'autore: ")
numero_pagine = input("inserisci il numero di pagine: ")

#creo l'oggetto "libro" con le variabili scelte dall'utente
nuovo_libro = Libro(titolo_utente, nome_autore, numero_pagine)

print("libro registrato con successo")
nuovo_libro.stampa_libro()

print = input("vuoi inserire il libro nella tua biblioteca personale? (si/no)")
if "si":
    print 
else:
    exit()
    
#"""book = input(f"inserisci {nome_libro}, {autore}, {pagine}")"""