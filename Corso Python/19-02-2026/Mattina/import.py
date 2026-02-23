import requests

risposta = requests.get("https://www.google.com")

print(risposta.text)

#risposta 200

"""ogni volta che andiamo su una pagina web ci restituisce il codice. 200 
la pagina esiste. 404 non esiste"""

"se salvo il print in un file html salverei il codice di quella pagina"