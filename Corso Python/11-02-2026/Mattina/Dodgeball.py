"""creare una classe Membrosquadra e una squadra che conterrà le diversi classi figlie che rappresentano ruoli specifici all'interno
della squadra di dodgeball, come giocatore, allenatore, e assistente (attaccanti, difensori, retriever i ruoli)

classe MembroSquadra:

Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)
Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro"""
import random

# ==========================================
# LIVELLO 1: CLASSE BASE (SUPERCLASSE)
# ==========================================
class MembroSquadra:
    """Rappresenta un membro generico di una società sportiva."""
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def descrivi(self):
        """Stampa le informazioni anagrafiche base."""
        print(f"Nome: {self.nome}, Età: {self.eta}")

# ==========================================
# LIVELLO 2: SPECIALIZZAZIONE (EREDITÀ)
# ==========================================
class Giocatore(MembroSquadra):
    """Estende MembroSquadra aggiungendo dati tecnici del giocatore."""
    def __init__(self, nome, eta, ruolo, n_maglia):
        # super() passa nome ed eta alla classe madre MembroSquadra
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.n_maglia = n_maglia
        # Stato fondamentale per la logica del gioco (Dodgeball)
        self.eliminato = False 

class Attaccante(Giocatore):
    """Sottoclasse specifica: ha il compito di lanciare la palla."""
    def lancia_palla(self):
        print(f" > {self.nome} carica il tiro...")

class Difensore(Giocatore):
    """Sottoclasse specifica: la sua forza è la resistenza ai colpi."""
    pass # Non ha metodi unici, le sue caratteristiche sono gestite dall'arbitro

class Retriever(Giocatore):
    """Sottoclasse specifica: non può essere eliminato e recupera palloni."""
    def recupera_palla(self):
        print(f"   (Il retriever {self.nome} corre a recuperare la palla)")

# ==========================================
# LIVELLO 3: COMPOSIZIONE (IL CONTENITORE)
# ==========================================
class Squadra:
    """Gestisce un gruppo di oggetti Giocatore e ne interroga lo stato."""
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = [] # Lista che conterrà oggetti di tipo Attaccante, Difensore, ecc.

    def aggiungi_giocatore(self, player):
        """Metodo per popolare la squadra con nuovi membri."""
        self.giocatori.append(player)

    def scegli_bersaglio(self):
        """
        Filtra i giocatori della squadra per trovare un bersaglio valido.
        Esclude i Retriever e chi è già stato eliminato.
        """
        disponibili = []
        for p in self.giocatori:
            # isinstance verifica se il giocatore appartiene a una certa classe
            if not isinstance(p, Retriever) and p.eliminato == False:
                disponibili.append(p)
        
        # Se la lista non è vuota, estrae un giocatore a caso
        if len(disponibili) > 0:
            return random.choice(disponibili)
        return None
    
    def scegli_attaccante(self):
        """Cerca tra i giocatori attivi chi ha il ruolo di Attaccante."""
        attaccanti = []
        for p in self.giocatori:
            if isinstance(p, Attaccante) and p.eliminato == False:
                attaccanti.append(p)
        
        if len(attaccanti) > 0:
            return random.choice(attaccanti)
        return None
    
    def ha_perso(self):
        """
        Controlla se la squadra è ancora in grado di giocare.
        La sconfitta avviene se Attaccanti e Difensori sono tutti eliminati.
        """
        vivi = 0
        for p in self.giocatori:
            # I Retriever non contano ai fini della sopravvivenza della squadra
            if not isinstance(p, Retriever) and p.eliminato == False:
                vivi += 1
        
        # Restituisce True se non ci sono più superstiti validi
        return vivi == 0
            

def gioca_partita(squadra_a, squadra_b):
    turno = 1
    
    # Il ciclo continua finché ENTRAMBE le squadre hanno ancora giocatori vivi
    while not squadra_a.ha_perso() and not squadra_b.ha_perso():
        print(f"\n--- TURNO {turno} ---")
        
        # 1. Capire chi attacca e chi difende
        if turno % 2 != 0:
            attaccante_team = squadra_a
            difensore_team = squadra_b
        else:
            attaccante_team = squadra_b
            difensore_team = squadra_a
            
        # 2. Selezionare i giocatori per questo turno
        lanciatore = attaccante_team.scegli_attaccante()
        bersaglio = difensore_team.scegli_bersaglio()
        
        # 3. Se abbiamo sia un lanciatore che un bersaglio, facciamo il tiro
        if lanciatore and bersaglio:
            # --- QUI DOBBIAMO METTERE LA LOGICA DEL DADO ---
            pass # Questo è un segnaposto, lo riempiremo ora
            
        # 4. Aumentiamo il turno per passare alla prossima fase
        turno += 1

    # Fuori dal ciclo, diciamo chi ha vinto
    if squadra_a.ha_perso():
        print(f"La squadra {squadra_b.nome} vince!")
    else:
        print(f"La squadra {squadra_a.nome} vince!")
            
p1 = Attaccante("Marco", 22, "Attaccante", 10)
p2 = Difensore("Luca", 25, "Difensore", 5)
p3 = Retriever("Sara", 20, "Retriever", 1)