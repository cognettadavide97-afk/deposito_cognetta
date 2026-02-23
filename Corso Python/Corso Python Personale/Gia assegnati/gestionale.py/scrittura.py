def scrittura(nome_file: str, registro: dict[str, list]) -> dict[str, list]:
    """
    Trasforma il dizionario in formato testo e lo salva sul file.
    Ogni riga sarà formattata come: Chiave,,voto1,voto2...
    """
    righe_testo = []

    for chiave, voti in registro.items():
        # Creiamo la riga partendo dalla chiave. 
        # Siccome la lettura del compagno cerca i voti dall'indice 2 in poi,
        # dobbiamo assicurarci che ci sia una virgola extra dopo la chiave.
        riga = chiave + ","
        
        # Aggiungiamo i voti separati da virgole
        for voto in voti:
            riga += "," + str(voto)
        
        righe_testo.append(riga)

    # Uniamo tutte le righe con un ritorno a capo
    testo_finale = "\n".join(righe_testo)

    with open(nome_file, "w") as file:
        file.write(testo_finale)

    return registro