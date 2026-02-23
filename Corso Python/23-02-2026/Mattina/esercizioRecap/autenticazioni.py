import csv
from utenti import Utente, Admin

def credenziali(nome, password):
    #creo/aggiorno i due file in un'unica stringa per pulizia codice
    with open("utenti.txt", "a") as file_nomi, open ("password.text", "a") as file_pw:
        file_nomi.write(nome + "\n") #file dei nomi
        file_pw.write(password + "\n") #file delle password
    print("Registrazione effettuata!")


def registra_utente():
    registrato = False #inizializzo condizione False per utente non registrato
    
    #se l'utente non è registrato, faccio partire il ciclo
    while not registrato: 
        registrazione = input("vuoi registrarti? (y/n)").lower()
        
        #se l'utente sceglie si, inserisce le nuove credenziali
        if registrazione == "y":
            nome_utente = input("inserisci nome utente: ").lower()
            pw_utente = input("inserisci una password: ")
            check_pw = input("inserisci nuovamente la password: ")
            
            if pw_utente == check_pw:
                #da modificare, perché altrimenti rischio di salvare su nomi
                print("Registrazione effettuata con successo!")
                registrato = True
                credenziali(nome_utente, pw_utente)
                
            else:
                print("Errore! le password non corrispondono")
        else:
            print("Operazione annullata")
            break
        
def verifica_login():
    
    nome_input = input("Nome utente: ").lower()
    pw_input = input("Password: ")
    
    #controllo Admin (credenziali hardcoded)
    rettore = Admin()
    if nome_input == rettore.username and rettore.check_credentials(pw_input):
        print("Benvenuto rettore")
        return rettore
    
    #controllo utenti base
    with open("utenti.txt", "r") as file_nomi, open ("password.text", "r") as file_pw:
        nomi = [linea.strip() for linea in file_nomi.readlines()]
        passwords = [linea.strip() for linea in file_pw.readlines()]
        
        if nome_input in nomi:
            indice = nomi.index(nome_input)
            if passwords[indice] == pw_input:
                print(f"Benvenuto {nome_input}!")
                return Utente(nome_input) # Restituiamo l'oggetto Utente
            else:
                print("Password errata")
        else:
            print("Credenziali errate.")
    