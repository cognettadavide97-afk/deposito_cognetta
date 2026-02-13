"""Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”."""

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        
    def emetti_suono(self):
        if self.specie == "Cane":
            print("Bau!")
        elif self.specie == "Lupo":
            print("Woof!")
        else:
            print("Miaooooo")
            
cane = Animale("Ares", "Cane")
lupo = Animale("Balto", "Lupo")
gatto = Animale("Kimba", "Gatto")

cane.emetti_suono() #Bau
lupo.emetti_suono() #Woof
gatto.emetti_suono() #Miaooo