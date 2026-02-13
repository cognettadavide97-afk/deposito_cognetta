"""Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”."""

class Persona:
    def __init__(self, nome, eta, sesso):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso
        
    def presentati(self):
        if self.nome == "Marco":
            print(f"ciao mi chiamo {self.nome} e ho {self.eta} anni")
        else:
            print(f"Ciao sono {self.nome} e sono {self.sesso},. Può sembrare strano ma è una storia vera")
        
p = Persona ("Marco", 32, "Maschio")
a = Persona ("Lucia", 16, "Sirena")
p.presentati()
a.presentati()

