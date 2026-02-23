def crea_alunno(nome_file: str, nome_alunno: str, voti_iniziali: list) -> dict[str, list]:
    """
    Aggiunge un nuovo alunno al dizionario e aggiorna il file.
    """
    # 1. Carichiamo il dizionario attuale (usando la funzione mandata dai compagni)
    registro: dict[str, list] = lettura(nome_file)

    # 2. Se l'alunno non esiste, lo aggiungiamo
    if nome_alunno not in registro:
        registro[nome_alunno] = voti_iniziali
        
        # 3. Salviamo il file e restituiamo il dizionario aggiornato
        return scrittura(nome_file, registro)
    
    print(f"L'alunno {nome_alunno} esiste già.")
    return registro
