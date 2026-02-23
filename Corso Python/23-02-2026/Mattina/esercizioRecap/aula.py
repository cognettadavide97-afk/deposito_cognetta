import csv

def aggiungi_studente():
    nome = input("Nome studente: ")
    corso = input("Corso: ")
    
    # Usiamo 'a' per non cancellare gli studenti già presenti, che verranno inseriti come nuova riga
    with open("studenti.csv", "a", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow([nome, corso])
    print("Studente aggiunto correttamente!")
    
def stampa_aula():
    try:
        with open("studenti.csv", "r") as file_csv:
            reader = csv.reader(file_csv)
            lista_studenti = list(reader)
            
            # Ordiniamo la lista in base al secondo elemento (indice 1: il Corso)
            # x[1] indica che vogliamo ordinare per la colonna 'Corso'
            lista_ordinata = sorted(lista_studenti, key=lambda x: x[1])
            
            print("\n--- ELENCO STUDENTI (Ordinati per Corso) ---")
            for studente in lista_ordinata:
                print(f"Studente: {studente[0]} | Corso: {studente[1]}")
    except FileNotFoundError:
        print("L'aula è ancora vuota.")
        
def modifica_studente():
    studenti = []
    # 1. Leggiamo tutto il file e salviamolo in una lista
    try:
        with open("studenti.csv", "r", newline="") as file_csv:
            reader = csv.reader(file_csv)
            studenti = list(reader) 
    except FileNotFoundError:
        print("Errore: Il file degli studenti non esiste ancora.")
        return

    # 2. Chiediamo chi modificare
    target = input("Inserisci il nome dello studente da modificare: ").lower()
    trovato = False
    
    for riga in studenti:
        # riga[0] è il nome, riga[1] è il corso
        if riga[0].lower() == target:
            nuovo_corso = input(f"Inserisci il nuovo corso per {riga[0]}: ")
            riga[1] = nuovo_corso  # Modifichiamo il dato nella lista
            trovato = True
            break # Usciamo dal ciclo una volta trovato
        
    if trovato:
        with open("studenti.csv", "w", newline="") as file_csv:
            writer = csv.writer(file_csv)
            writer.writerows(studenti) # Scrive l'intera lista aggiornata
        print("Modifica salvata con successo!")
    else:
        print(f"Studente '{target}' non trovato in elenco.")