class Utente:
    def __init__(self, username):
        self.username = username
        
class Admin(Utente):
    def __init__(self):
        
        #Passo admin alla classe padre. Hardcoding Admin
        super().__init__("Admin")
        #Password con name mangling
        self.__pw_sys = "Root123"
        
    #poiché l'attributo pw è privato, creo una funzione di verifica
    def check_credentials(self, pw_digitata):
        return self.__pw_sys == pw_digitata 
    
    #funzione specifica della classe admin, reset dati
    def reset_dati(self, motivazione):
        # 1. Reset della lista studenti (quella del file CSV)
        # Aprire in 'w' senza scrivere nulla svuota il file automaticamente
        with open("studenti.csv", "w") as f:
            pass 
        
        # 2. Registrazione dell'intervento (Logging)
        # La traccia chiede un file chiamato 'intervento utente' con la motivazione
        with open("intervento_utente.txt", "a") as log:
            log.write(f"Reset Aula effettuato. Motivazione: {motivazione}\n")
            
        print("Lista studenti cancellata e intervento registrato!")