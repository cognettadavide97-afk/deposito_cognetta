import Gestione_Utenti as gu
import Controllo_Utenti as cu

def avvia_sistema():
    gestore = cu.GestoreAccessi()

    # Database pre-caricato
    database_utenti = [
        gu.Dipendente("Mario", "Rossi", "DIP01", "Sviluppo"),
        gu.Dipendente("Elena", "Verdi", "DIP02", "Marketing"),
        gu.Esterno("Andrea", "Neri", "EST01", "Server", "2026-12-31") # Ricordati di aggiungere Esterno in gu!
    ]

    # Assegnazione badge
    for u in database_utenti:
        u.badge = gu.Badge(f"SN-{u._id_univoco}")

    while True:
        print("\n--- TERMINALE AZIENDALE ---")
        login_id = input("Inserisci ID Univoco (o 'exit'): ").strip().upper()

        if login_id == 'EXIT': break

        # Ricerca utente
        utente = next((u for u in database_utenti if u._id_univoco == login_id), None)

        if utente:
            print(f"Riconosciuto: {utente.nome} {utente.cognome} ({type(utente).__name__})")
            print("1. Timbra ENTRATA")
            print("2. Timbra USCITA")
            print("3. Visualizza Report (Admin)")
            
            scelta = input("Cosa vuoi fare? ")

            if scelta == "1":
                gestore.registra_movimento(utente, "ENTRATA")
            elif scelta == "2":
                gestore.registra_movimento(utente, "USCITA")
            elif scelta == "3":
                gestore.mostra_report_accessi()
            else:
                print("Opzione non valida.")
        else:
            print("ID non trovato.")

if __name__ == "__main__":
    avvia_sistema()