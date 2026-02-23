"""Scrivi una funzione che prende una stringa e restituisce la stringa invertita."""

def inverti_stringa(stringa): #valore fittizio serve a capire cosa sto facendo concettualmente. nome funzione cosa fa la funzione
    nuova_stringa = stringa[::-1] #slicing della stringa [:inzio:fine:passo]
    return nuova_stringa #return è lo strumento per "tirare fuori" la funzione
    
#ora che abbiamo creato la funzione la utilizziamo e invertiamo una stringa che assegneremo come valore

risultato = inverti_stringa("caccapupu")
print(risultato)

