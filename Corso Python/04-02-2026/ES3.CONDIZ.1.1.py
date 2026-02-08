"""Creare un if con else semplice, dentro l'if inserire una struttura di creazione dati
(nome, passowrd, id dato dal sistema a crescere) e nell'else il controllo automatico la dove è
presente l'account nel sistema e solo se si passa all'else concludere lo script"""

account = [("davide", "python123", "001"), ("mirko", "OOP123", "002")]
#creo un valore numero tramite len(account) che mi restituisce un numero che chiameremo "id utente"
len(account)

#FASE DI LOGIN
print("Benvenuto! Prego inserisca le credenziali di accesso")
nome = input("inserisci nome: ").lower().strip()
password = input("inserisci password" )

#creo un controllo preliminare degli utenti già registrati
#non uso il for per richiesta della traccia (sarebbe stato molto meglio)
id_registrati = [account[0][0], account[1][0]]

if nome in id_registrati:
    print("Bentornato", nome, "!")
else:
    registrazione = input("Utente non registrato. Vuoi reigstrare un account? (si/no)").lower()
    #forzo l'utente ad utilizzare come comando si o no
    while registrazione not in ["si", "no"]: #scusami Mirko, sono uscito un po' fuori traccia qui :p
        registrazione = input("Vuoi registrare un account? (si/no): ").lower()
    if registrazione == "si": #reinserisco la richiesta delle credenziali
        nuovo_nome = input("inserisci nome: ").lower().strip()
        conferma_nome = input(f"Vuoi utilizzare {nuovo_nome} come nome? (si/no)").lower()
        while conferma_nome not in ["si", "no"]: #scusami Mirko, sono uscito un po' fuori traccia qui :p
            conferma_nome = input(f"Vuoi utilizzare {nuovo_nome} come nome? (si/no)").lower()
        while conferma_nome == "no":#fuori traccia
            nuovo_nome = input("inserisci nome: ").lower().strip()
            conferma_nome = input(f"Vuoi utilizzare {nuovo_nome} come nome? (si/no)").lower()
        #anche qui forzare blocco su si o no
        #inserire un ciclo while? se l'utente no deve poter scegliere nuovamente il nome
        nuova_password = input("inserisci password:" )
        #necessaria una stringa che permetta la conferma della password
        conferma_password = input("conferma la password")
        #ciclo while per evitare che l'utente vada avanti se inserisce due password diverse
        while conferma_password != nuova_password:#sono andato fuori traccia ma purtroppo sono perfezionista.
            print("le password non corrispondono!")
            nuova_password = input("inserisci password:" )
            conferma_password = input("conferma la password")
        # Calcolo l'ID basandomi su quanti account ci sono in QUESTO momento
        nuovo_id = len(account) + 1
        formattazione_id = str(nuovo_id).zfill(3)
        account.append((nuovo_nome, nuova_password, formattazione_id))
        print("Congratulazioni! Ora sei registrato al sito")
    else:
        exit()
print("fine")
print(account)