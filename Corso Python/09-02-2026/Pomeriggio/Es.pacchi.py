class Pacco:
    def __init__(self, codice, peso, stato="in magazzino"):
        self.codice = codice
        self.peso = peso  
        self.stato = stato
    
    def mostra_info(self):
        print(f"codice pacco: {self.codice}, peso: {self.peso}, stato: {self.stato}")
        
    def aggiorna_stato(self, nuovo_stato):
        self.stato = nuovo_stato
        print(f"Stato aggiornato! Il pacco {self.codice} ora è: {self.stato}")
    
class Magazzino:
    def __init__(self):
        self.inventario = {}
        
    def aggiungi_pacco(self, pacco):
        self.inventario[pacco.codice] = pacco
        
    def cerca_per_codice(self, codice):
        #restituiamo l'oggetto trovato nel dizionario
        return self.inventario.get(codice)
        
    
    def filtra_per_stato(self, stato):
        print(f"\n--- Elenco pacchi con stato: {stato} ---")
        for pacco in self.inventario.values():
            if pacco.stato == stato:
                pacco.mostra_info()
    
class Gestorepacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino
    
    def avvia_consegna(self, codice):
        pacco = self.magazzino.cerca_per_codice(codice)
        if pacco:
            pacco.aggiorna_stato("in consegna")
    
    def conferma_consegna(self, codice):
        pacco = self.magazzino.cerca_per_codice(codice)
        if pacco:
            pacco.aggiorna_stato("pacco consegnato")
    
    def calcola_peso_non_consegnati(self):
        totale = 0
        for pacco in self.magazzino.inventario.values():
            if pacco.stato != "consegnato":
                totale += pacco.peso
        return totale
    
#creiamo il magazzino "fisico", poi il gestore che lo controlla
mio_magazzino = Magazzino()
mio_gestore = Gestorepacchi(mio_magazzino)

# Grazie al valore di default, non serve scrivere "in magazzino" ogni volta
p1 = Pacco("P001", 1.5)
p2 = Pacco("P002", 3.2)
p3 = Pacco("P003", 0.5)
p4 = Pacco("P004", 12.0)
p5 = Pacco("P005", 7.8)

#REGISTRAZIONE NEL MAGAZZINO
# Dobbiamo "caricarli" nell'inventario
mio_magazzino.aggiungi_pacco(p1)
mio_magazzino.aggiungi_pacco(p2)
mio_magazzino.aggiungi_pacco(p3)
mio_magazzino.aggiungi_pacco(p4)
mio_magazzino.aggiungi_pacco(p5)

# SIMULAZIONE OPERAZIONI (come richiesto dal compito)
# Avviamo una consegna e ne completiamo un'altra
mio_gestore.avvia_consegna("P001")     # Stato: in consegna
mio_gestore.conferma_consegna("P002")  # Stato: consegnato

# STAMPA DEI RISULTATI
# Vediamo chi è ancora in magazzino e chi è in viaggio
mio_magazzino.filtra_per_stato("in magazzino")
mio_magazzino.filtra_per_stato("in consegna")

# STAMPA DEI RISULTATI
# Vediamo chi è ancora in magazzino e chi è in viaggio
mio_magazzino.filtra_per_stato("in magazzino")
mio_magazzino.filtra_per_stato("in consegna")