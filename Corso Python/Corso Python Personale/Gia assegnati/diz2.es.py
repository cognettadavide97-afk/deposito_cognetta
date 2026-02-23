"""Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10"""

registro = {}

while True:
    nome = input("Inserisci nome alunno (o 'fine' per uscire): ")
    if nome.lower() == 'fine':
        break
    
    voto = input(f"Inserisci la media di {nome}: ")
    registro[nome] = voto

print(f"Registro classe: {registro}")


"""alunno1 = {"alunno": "Giovanni", "media": 7.5}
alunno2 = {"alunno": "Alfredo", "media": 9}
alunno3 = {"alunno": "Michela", "media": 10}

classe = {1:alunno1,
          2:alunno2,
          3:alunno3}"""

"""comando = input("inserisci 'media' per visualizzare la media degli studenti: ")
if comando == "media":
    for alunno, dati in classe.items():
        nome = dati["alunno"]
        media = dati["media"]
        print(f"Nome: {nome}, Media: {media}")
        
for dati in classe.values():
    print(f"Nome: {dati["alunno"]}, Media: {dati["media"]}")"""