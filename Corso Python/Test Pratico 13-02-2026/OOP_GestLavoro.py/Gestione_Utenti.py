from abc import ABC, abstractmethod
from datetime import datetime

# --- ASTRAZIONE ---
class Persona(ABC):
    def __init__(self, nome, cognome, id_univoco):
        self.nome = nome
        self.cognome = cognome
        # Incapsulamento: l'ID è protetto, non vogliamo che venga cambiato a caso
        self._id_univoco = id_univoco 
        self.badge = None

    @abstractmethod
    def get_permessi(self):
        """Metodo astratto: ogni sottoclasse deve decidere i propri permessi"""
        pass

# --- INCAPSULAMENTO (Oggetto di supporto) ---
class Badge:
    def __init__(self, codice_seriale):
        self.__codice_seriale = codice_seriale  # Privato, doppio underscore per Name mangling.
        self.attivo = True
        self.data_emissione = datetime.now()

    def get_seriale(self):
        return self.__codice_seriale

# --- EREDITARIETÀ ---
class Dipendente(Persona):
    def __init__(self, nome, cognome, id_univoco, reparto):
        super().__init__(nome, cognome, id_univoco)
        self.reparto = reparto

    def get_permessi(self):
        # Un dipendente ha accesso totale (o quasi)
        return f"Accesso Completo per reparto {self.reparto}"

class Visitatore(Persona):
    def __init__(self, nome, cognome, id_univoco, ditta_provenienza):
        super().__init__(nome, cognome, id_univoco)
        self.ditta_provenienza = ditta_provenienza

    def get_permessi(self):
        # Un visitatore ha permessi limitati
        return f"Accesso Limitato (Ospite di: {self.ditta_provenienza})"
    
    # Aggiungi questo in fondo a Gestione_Utenti.py

class Esterno(Persona): # Ereditarietà
    def __init__(self, nome, cognome, id_univoco, specializzazione, scadenza_contratto):
        super().__init__(nome, cognome, id_univoco)
        self.specializzazione = specializzazione
        self.scadenza_contratto = scadenza_contratto

    def get_permessi(self): # Polimorfismo
        return f"Accesso Tecnico: {self.specializzazione} (Valido fino al {self.scadenza_contratto})"