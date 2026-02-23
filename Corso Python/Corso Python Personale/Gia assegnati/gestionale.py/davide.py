def crea_alunno(nome_file: str, nome_alunno: str, voti_iniziali: list) -> dict[str, list]:
    """
    Aggiunge un nuovo alunno al dizionario e aggiorna il file.
    """
    # 1. Carichiamo il dizionario attuale
    registro: dict[str, list] = lettura(nome_file)

    # 2. Se l'alunno non esiste, lo aggiungiamo
    if nome_alunno not in registro:
        registro[nome_alunno] = voti_iniziali
        
        # 3. Salviamo il file e restituiamo il dizionario aggiornato
        return scrittura(nome_file, registro)
    
    print(f"L'alunno {nome_alunno} esiste già.")
    return registro

def scrittura(nome_file: str, registro: dict[str, list]) -> dict[str, list]:
    """
    Trasforma il dizionario in formato testo e lo salva sul file.
    Ogni riga sarà formattata come: Chiave,,voto1,voto2...
    """
    righe_testo = []

    for voti in registro.items():
        
        # Aggiungiamo i voti
        for voto in voti:
            riga += "," + str(voto)
        
        righe_testo.append(riga)

    # Uniamo tutte le righe con un ritorno a capo
    testo_finale = "\n".join(righe_testo)

    with open(nome_file, "w") as file:
        file.write(testo_finale)

    return registro
