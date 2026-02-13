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

#creo una classe sistema di accesso
class SistemaAccesso:
    def __init__(self):
        # Database simulato: {username: password}
        self.database_clienti = {}
        # Admin pre-inserito come richiesto dalla traccia
        self.admin_credenziali = {"Davide": "12345"}

    def registra_cliente(self):
        nome = input("Scegli un username: ")
        pw = input("Scegli una password: ")
        if nome in self.database_clienti or nome in self.admin_credenziali:
            print("Errore: Nome già occupato!")
            return None
        self.database_clienti[nome] = pw
        print(f"Benvenuto {nome}, registrazione effettuata!")
        return nome # Restituisco il nome per confermare l'avvenuto login

    def login(self):
        nome = input("Username: ")
        pw = input("Password: ")
        
        # Controllo se è Admin
        if nome in self.admin_credenziali and self.admin_credenziali[nome] == pw:
            return "admin"
        # Controllo se è Cliente
        elif nome in self.database_clienti and self.database_clienti[nome] == pw:
            return "cliente"
        else:
            print("Credenziali errate!")
            return None
    
"""#creo la classe "Negozio" compresa di nome 
#creo un dizionario "inventario"
#creo un metodo per gli articoli compreso di nome, prezzo e qta che verranno poi inserite nell'inventario
class Negozio:
    def __init__(self, nome):
        self.nome = nome
        
        #creo un attributo inventario da riempire
        self.inventario = {}
        #creo un attributo che mi permetta di controllare il guadagno del negozio
        self.guadagno = 0
    
    #aggiungo un metodo per poter riempire l'inventario con la creazione di articoli
    def aggiungi_articolo(self, nome_art, prezzo, qta):
        #creo la chiave nome_art a cui sono assegnati i valori di prezzo e qta
        self.inventario[nome_art] = {"prezzo": prezzo, "qta": qta}
        
              
              
#creo un sistema di login per verificare se chi accede è utente o amministratore
#se è amministratore
#aggiungo input che mi permette di visualizzare cosa è disponibile in inventario, di agg o rimuovere
#interfaccia che notifica l'amministratore del guadagno totale del negozio
#se è cliente: creo input di visualizzazione per un cliente
#creo input di selezione per cliente
#salvo i dati degli acquisti dei clienti una volta che hanno finito di comperare.
#salvo in una lista o dizionario con .append"""
