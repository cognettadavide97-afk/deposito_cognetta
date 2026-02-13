"""Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio 
che deve interagire con clienti, gestire l'inventario e permettere agli amministratori di supervisionare 
le operazioni. Il sistema sarà strutturato in tre parti principali: Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).
Amministrazione:
l'analisi del negozio da parte degli amministratori.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo 
un login e una registrazione, nonché fornire gli strumenti necessari per la manutenzione e 
l'analisi del negozio da parte degli amministratori"""

class Negozio:
    def __init__(self, nome):
        #inserisco l'attributo che darà nome al negozio
        self.nome = nome
        
        #inserisco un inventario, vuoto, che verrà aggiornato con gli articoli
        self.inventario = {}
        
    #inventario
    #inserisco dei metodi che mi permettono di aggiungere, modificare o rimuovere articoli 
    def aggiungi_articolo(self, nome_art, prezzo, qta):
        self.inventario[nome_art] = {
        "prezzo": prezzo,
        "qta": qta}
        print(f"{nome_art} aggiunto all'inventario.")

    def modifica_articolo(self, nome_art, nuovo_prezzo, nuova_qta):
        if nome_art in self.inventario:
            self.inventario[nome_art]["prezzo"] = nuovo_prezzo
            self.inventario[nome_art]["qta"] = nuova_qta
            print(f"{nome_art} aggiornato.")
        else:
            print("Articolo non trovato.")

    def rimuovi_articolo(self, nome_art):
        if nome_art in self.inventario:
            del self.inventario[nome_art]
            print(f"{nome_art} rimosso.")
        else:
            print("Articolo non trovato.")
            
    #mostra inventario permette all'utente di visionario gli articoli disponibili
    def mostra_inventario(self):

        if not self.inventario:
            print("Inventario vuoto.")
        return   # esce solo se vuoto



    
    #acquisto
    #inserisco funzioni che diano la possibilità di acquistare
    def vendi(self, nome_art):
        pass
    
#creo una classe utente con gli clienti e gli admin
class Utente:
    def __init__(self):
        #davide = nome admin, chiave. valore/pass 12345
        self.admin = {"Davide": 12345}
        self.clienti = {}
        
    def registra_cliente(self):
        nome = input("Username: ")
        pw = input("Password: ")

        # Controllo ADMIN
        if nome in self.admin and self.admin[nome] == pw:
            print("Accesso come ADMIN")
            return "admin"

        # Controllo CLIENTE ESISTENTE
        elif nome in self.clienti and self.clienti[nome] == pw:
            print("Accesso come cliente")
            return "cliente"

        # Username esiste ma password sbagliata
        elif nome in self.clienti or nome in self.admin:
            print("Password errata")
            return None

        # NUOVA REGISTRAZIONE
        else:
            self.clienti[nome] = pw
            print("Registrazione completata! Sei un nuovo cliente.")
            return "cliente"
