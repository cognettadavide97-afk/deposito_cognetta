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

#creazione delle classi

#creo l'inventario o magazzino
class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.acquisti = []
        
    def compra(self, negozio, nome_art, qta):
        # prova ad acquistare dal negozio
        successo = negozio.vendi(self, nome_art, qta)
        if successo:
            # se l'acquisto va a buon fine, memorizzo l'acquisto
            self.acquisti.append((nome_art, qta))


        
    
#creo la classe "Negozio" compresa di nome 
#creo un dizionario "inventario"
#creo un metodo per gli articolo compreso di nome, prezzo e qta che verranno poi inserite nell'inventario
class Negozio:
    def __init__(self, nome):
        self.nome = nome
    
     # inventario: dizionario
        # chiave = nome articolo
        # valore = dizionario con prezzo e quantità
        self.inventario = {}
              
#creo l'inventario
    
    def aggiungi_articolo(self, nome_art, prezzo, qta):
        self.inventario[nome_art] = {"prezzo": prezzo, "quantita": qta}
        print("Aggiunto:", nome_art, "- prezzo:", prezzo, "€ - qta:", qta)
        
    def aggiorna_articolo(self, nome_art, nuovo_prezzo=None, nuova_qta=None):
        if nome_art in self.inventario:
            if nuovo_prezzo is not None:
                self.inventario[nome_art]["prezzo"] = nuovo_prezzo
            if nuova_qta is not None:
                self.inventario[nome_art]["quantita"] = nuova_qta
            print("Articolo aggiornato:", nome_art, self.inventario[nome_art])
        else:
            print("Articolo non trovato:", nome_art)



#programma principale
#creo un sistema di login per verificare se chi accede è utente o amministratore
registrazione = input("sei un utente già registrato?: (si/no)").lower().strip()
if registrazione == "si":
    credenziali = input("prego inserire credenziali: ")
    if credenziali == "//":
        pass
    else:
        pass
elif registrazione == "errore":
    print("errore, per favore scrivi 'si' o 'no'")
    pass
else:
    richiesta_registrazione = input("vuoi registrarti al sito? (si/no)")
    if richiesta_registrazione == "si":
        print = input("Inserire credenziali: ")

#se è amministratore
#aggiungo input che mi permette di visualizzare cosa è disponibile in inventario, di agg o rimuovere
#interfaccia che notifica l'amministratore del guadagno totale del negozio
#se è cliente: creo input di visualizzazione per un cliente
#creo input di selezione per cliente
#salvo i dati degli acquisti dei clienti una volta che hanno finito di comperare.
#salvo in una lista o dizionario con .append
