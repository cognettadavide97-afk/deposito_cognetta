"""scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 anni
il programma dovrebbe stampare "mi dispiace,non puoi vedere questo film". Altrimenti
dovrebbe stampare "puoi vedere questo film"""

eta = input("prego inserisca la sua età: ")

#piccolo step di conferma con isdigit per evitare che il codice crashi se l'utente non inserisce un numero
if eta.isdigit():
    eta_input = int(eta) 
    if eta_input < 18:
        print("mi dispiace, non puoi vedere questo film")
    else:
        print("puoi vedere questo film")
else:
    print("per favore inserisci un valore numerico!")