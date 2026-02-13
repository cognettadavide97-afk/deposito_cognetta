"""studente = {"nome": "Alice",
            "eta": 20,
            "sesso": "Femmina"}

studente["città"] = "Roma"
print(studente)

#output {'nome': 'Alice', 'eta': 20, 'sesso': 'Femmina', 'città': 'Roma'}

#cambio il nome
giocatore = {"nome": "Ronaldo",
             "eta": 20,
             "sesso": "maschio"}
giocatore["Squadra"] = "Bayer Monaco"
print(giocatore)

#modifico cose a caso per testare errori
studente = {"nome": "Alice",
            "eta": 20,
            "sesso": "Femmina"}

studente["nome"] = "Roma"
print(studente)

#modifico2
studente = {"nome": "Alice",
            "eta": 20,
            "sesso": "Femmina"}

studente["Alice"] = "Roma"
print(studente)"""

#modifico3
studente = {"nome": ["Alice", "Marco", "Luca",], #si usa una lista per più valori (o tuple)
            "eta": 20,
            "sesso": "Femmina"}

studente["città"] = "Roma"
print("nome")
print(studente.keys())
print(studente.values())
print(studente)
print(studente["nome"])
print(studente["nome"][0])
print(studente.get("nome"))
print(studente.get("cognome"))