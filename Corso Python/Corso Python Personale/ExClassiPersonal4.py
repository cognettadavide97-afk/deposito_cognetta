"""Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% 
e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio 
“Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”."""

class Impiegato():
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio
        
    def aumenta_stipendio(self):
        if self.cognome == "Cognetta" and self.matricola == 12346:
            self.stipendio *= 1.1
        else:
            None
            
            """#ALTERNATIVA
    def aumenta_stipendio(self, percentuale):
        aumento = self.stipendio * (percentuale / 100)
        self.stipendio = self.stipendio + aumento"""
        
    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio: {self.stipendio}€")
        
Davide = Impiegato("Davide", "Cognetta", 12346, 9999)
Mario = Impiegato("Mario", "Rossi", 12345, 9999)

Davide.stampa_dettagli()
Davide.aumenta_stipendio()
Davide.stampa_dettagli()
Mario.stampa_dettagli()