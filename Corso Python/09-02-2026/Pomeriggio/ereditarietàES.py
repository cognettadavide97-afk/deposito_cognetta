"""Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
Classi parallele:
Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario."""

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione 
    
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_mesi):
        # Usiamo 'super()' per richiamare il costruttore della classe Prodotto
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia_mesi = garanzia_mesi  # Attributo specifico

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale  # Attributo specifico

class Fabbrica():
    def __init__(self):
        self.inventario = {}
        
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Aggiunti {quantita} pezzi di {prodotto.nome}.")
    
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto_totale = prodotto.calcola_profitto() * quantita
            print(f"Venduti {quantita} di {prodotto.nome}. Profitto: €{profitto_totale}")
        else:
            print(f"Errore: Scorte insufficienti per {prodotto.nome}!")
        
    def resi_prodotto(self, prodotto, quantita):
    # Il reso è essenzialmente un'aggiunta di magazzino
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
            print(f"Reso effettuato: {quantita} pezzi di {prodotto.nome} rientrati.")
            
# 1. Creiamo la nostra fabbrica
mia_fabbrica = Fabbrica()

# 2. Creiamo dei prodotti specifici
smartphone = Elettronica("iPhone 15", 500, 900, 24)
maglietta = Abbigliamento("T-shirt Cotone", 5, 20, "Cotone Organico")

# 3. Gestiamo il magazzino
mia_fabbrica.aggiungi_prodotto(smartphone, 10)
mia_fabbrica.aggiungi_prodotto(maglietta, 50)

# 4. Simuliamo una vendita
mia_fabbrica.vendi_prodotto(smartphone, 2)  # Profitto: (900-500) * 2 = 800

# 5. Gestiamo un reso
mia_fabbrica.resi_prodotto(maglietta, 1)