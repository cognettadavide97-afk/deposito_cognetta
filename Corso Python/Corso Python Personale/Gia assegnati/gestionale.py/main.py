# Trasformate il programma che abbiamo creato in
# precedenza per la gestione dei voti degli alunni in un
# programma per la gestione di una classe che utilizza un
# file come database:
# All’avvio il programma chiede se si vuole leggere l’elenco
# degli alunni e i loro voti e medie, se si vuole aggiungere un
# alunno o un voto

# dizionario = lettura()
def lettura(nome_file: str) -> dict[str, list]:
    
    res: dict = {}

    try:
        with open(nome_file, "r") as file:
            raw = file.read()
            if not raw:
                return res
        

        rows = raw.split("\n")

        for row in rows:
            
            splitted_row = row.split(",")
            
            key = (splitted_row[0].strip() + splitted_row[1]).strip()
            if key not in res:
                res[key] = []

            for i in range(2, len(splitted_row)):
                res[key].append(splitted_row[i].strip())

    except FileNotFoundError:
        print("Errore: Il file specificato non è stato trovato nella cartella!")
        with open(nome_file, "x"):
            pass
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")
    finally:
        return res

def media_voti(alunno: str, dizionario: dict):
    voti = dizionario.get(alunno)
    media = sum(voti)/len(voti)
    print(f"L'alunno {alunno} ha media {media}")
    return media

def aggiungi_voto(alunno:str, dizionario:dict, new_voto:float):
    if alunno in dizionario:
        dizionario[alunno].append(new_voto)
        return dizionario
    else:
        print("alunno non trovato")
        return False
        
def crea_alunno(dizionario:dict, nome_alunno: str, voti_iniziali: list) -> dict[str, list]:
    """
    Aggiunge un nuovo alunno al dizionario e aggiorna il file.
    """
    if voti_iniziali != []:
        voti_iniziali = voti_iniziali.split(",")
    else:
        return False
    # 1. Se l'alunno non esiste, lo aggiungiamo
    if nome_alunno not in dizionario:
        dizionario[nome_alunno] = voti_iniziali
        return dizionario
    
    print(f"L'alunno {nome_alunno} esiste già.")
    return False

def scrittura(nome_file: str, dizionario: dict[str, list]) -> dict[str, list]:
    """
    Trasforma il dizionario in formato testo e lo salva sul file.
    Ogni riga sarà formattata come: Chiave,,voto1,voto2...
    """
    righe_testo = []

    for voti in dizionario.items():
        
        # Aggiungiamo i voti
        riga = ""
        for voto in voti:
            riga += "," + str(voto)
        
        righe_testo.append(riga)

    # Uniamo tutte le righe con un ritorno a capo
    testo_finale = "\n".join(righe_testo)

    with open(nome_file, "w") as file:
        file.write(testo_finale)

    return dizionario

def stampa_classe(dizionario):
    if dizionario:
        print(f"{'ALUNNO':<15} | {'VOTI':<15} | {'MEDIA':<5}")
        print("-" * 45)
        
        for alunno in dizionario:
            voti = dizionario[alunno]  
            media = media_voti(alunno, dizionario)
            
            # Parsing dei voti in str
            voti_str = ", ".join(map(str, voti))
            
            # Stampa tutto 
            print(f"{alunno:<15} | {voti_str:<15} | {media:>5.2f}")
            #{'Marco': [7, 8, 6], 'Anna': [9, 9, 10]}
    else:
        print("clase ancora vuota")
    
def check_value(stringa, tipo_atteso):
    try:
        valore_convertito = tipo_atteso(stringa)
        return valore_convertito
    except ValueError:
        return False
    
    
def play():
    nome_file = "classe.csv"
    dizionario = lettura(nome_file)
    print("DEBUG:," , dizionario)
    print( "connessione al db eseguita")
    
    while True:
            
        print("1) leggi elenco alunni \n2) aggiungi alunno\n3) aggiungi voto")
        user = input("quale azione vuoi fare?")
        scelta = None
        
    
        if user in ("1", "2", "3"):
            check_value(user, int)
            scelta = user
        else: 
            print("devi inserire una opzione valida")
      
        if scelta:
            match scelta:
                case "1":
                    stampa_classe(dizionario)

                case "2":
                    while True:
                        new_nome = input("inserisci nome del nuovo alunno : ").capitalize()

                        if check_value(new_nome, int):
                            print("devi inserire una stringa")
                            break       
                                             
                        voti_iniziali = input(f"inserisci  i voti per aluno {new_nome} separati da ',' : ")
                        if not crea_alunno(dizionario, new_nome, voti_iniziali):
                            print("ERRORE!")
                        scrittura(nome_file, dizionario)
                        break
                
                case "3":
                    while True:
                        alunno = input("a quale alunno vuoi aggiungere voto?")
                        if check_value(new_nome, int):
                            print("devi inserire una stringa")
                            break
                        
                        new_voto = input(f"inserisci nuovo voto a {alunno}: ")
                        if not aggiungi_voto(alunno, dizionario, new_voto): 
                            print("ERRORE!")
                            scrittura(nome_file, dizionario)
                            break
                    
                
        if input("vuoi fare un'altra operazione? (y/n)") != "y":
            break
        scrittura
play()


     
     