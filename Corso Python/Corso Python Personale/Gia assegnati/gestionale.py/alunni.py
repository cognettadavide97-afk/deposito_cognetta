registro = {}

while True:
    nome = input("Inserisci nome alunno (o 'fine' per uscire): ")
    if nome.lower() == 'fine':
        break
    
    voto = input(f"Inserisci la media di {nome}: ")
    registro[nome] = voto

print(f"Registro classe: {registro}")



"""Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto"""

import csv

def scrittura(nome_file: str, registro: dict[str, list]) -> None:
    """
    Riceve il dizionario della classe e lo salva in formato CSV.
    Ogni riga del file sarà: nome,voto1,voto2,voto3...
    """
    # Apriamo il file in modalità 'w' (scrittura). 
    # encoding='utf-8' serve per gestire correttamente eventuali accenti nei nomi.
    with open(nome_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Iteriamo attraverso il dizionario: nome (chiave) e voti (valore/lista)
        for nome, voti in registro.items():
            # Creiamo la riga da scrivere: mettiamo il nome in una lista 
            # e la uniamo alla lista dei voti.
            riga = [nome] + voti
            
            # Scriviamo la riga completa nel file CSV
            writer.writerow(riga)
            
    print(f"File '{nome_file}' aggiornato con successo.")