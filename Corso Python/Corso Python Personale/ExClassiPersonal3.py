"""Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, 
ad esempio “Questa è una Toyota Corolla del 2017”."""

class Automoboile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")
        
auto = Automoboile ("Toyota", "Corolla", "2017")
auto.descrivi()