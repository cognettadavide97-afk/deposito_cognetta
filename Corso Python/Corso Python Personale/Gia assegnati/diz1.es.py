"""Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}"""


stringa = "apelle figlio di apollo fece una palla di pelle di pollo" #testo in una variabile

diz_frequenze = {carattere: stringa.count(carattere) for carattere in stringa}

print(diz_frequenze)

frequenze = {}
for carattere in stringa:
    if carattere in frequenze:
        # Se la lettera è già nel dizionario, aumento il conteggio
        #frequenze[carattere] = frequenze[carattere] + 1
        frequenze[carattere] += 1
    else:
        # Se è la prima volta che vedo questa lettera, inizio da 1
        frequenze[carattere] = 1

print(frequenze)
    