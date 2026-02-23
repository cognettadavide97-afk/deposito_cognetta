from autenticazioni import registra_utente, verifica_login
from aula import aggiungi_studente, stampa_aula, modifica_studente
from utenti import Admin

def menu_operazioni(utente_loggato):
    """Sottomenu per le azioni dopo il login"""
    while True:
        print(f"\n--- Area Riservata: {utente_loggato.username} ---")
        print("1. Inserisci o Modifica Studenti")
        print("2. Stampa l'aula (Ordinata per Corso)")
        
        # Opzione speciale visibile solo se l'utente è Admin
        if isinstance(utente_loggato, Admin):
            print("3. Reset Totale Sistema (Solo Admin)")
            
        print("4. Logout")
        
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            azione = input("Vuoi (A)ggiungere o (M)odificare? ").lower()
            if azione == "a":
                aggiungi_studente()
            elif azione == "m":
                modifica_studente()
        
        elif scelta == "2":
            stampa_aula()
            
        elif scelta == "3" and isinstance(utente_loggato, Admin):
            motivo = input("Inserisci la motivazione del reset: ")
            utente_loggato.reset_dati(motivo) # Richiama la funzione che abbiamo appena scritto
            
        elif scelta == "4":
            print("Logout effettuato.")
            break
        else:
            print("Opzione non valida.")

def main():
    """Punto di ingresso principale"""
    while True:
        print("\n=== SISTEMA GESTIONE SCOLASTICA ===")
        print("1. Registrazione nuovo utente")
        print("2. Login")
        print("3. Esci dal programma")
        
        scelta_iniziale = input("Cosa vuoi fare? ")

        if scelta_iniziale == "1":
            registra_utente() # Dal modulo autenticazioni
            
        elif scelta_iniziale == "2":
            # verifica_login restituisce un oggetto Utente o Admin, oppure None
            utente = verifica_login() 
            if utente:
                menu_operazioni(utente) # Passiamo l'oggetto al sottomenu
                
        elif scelta_iniziale == "3":
            print("Chiusura del programma. Arrivederci!")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
        
        
        
    
    