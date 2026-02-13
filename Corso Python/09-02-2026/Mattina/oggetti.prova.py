class persona():
    pass

mirko_OBJ = persona()#sto creando un nuovo oggetto
#classi con maiuscola
#non ho un costruttore dentro la classe (init) ma è presente, perché esiste di defualt, seppur vuoto

class persona():
    
    x = 10
    def __init__(self): #in questo caso il costruttore è presente e la variabile x=10 è di tutti gli OBJ persona
        pass

mirko_OBJ = persona() 
print(mirko_OBJ)

"""----------------------------------------------------------------------------------------------------"""

class Automobile:                           # dichiaro la classe

    numero_di_ruote = 4                       # attributo di classe

    def __init__(self, marca, modello):       # metodo costruttore

        self.marca = marca                  # attributo di istanza

        self.modello = modello              # attributo di istanza

    def stampa_info(self):                    # metodo di istanza

        print("L'automobile è una", self.marca, self.modello)
        
"""--------------------------------------------------------------------------------------------------"""
auto1 = Automobile("Fiat", "500")    # crea un oggetto di Automobile

auto2 = Automobile("BMW", "X3")      # crea un altro oggetto di Automobile

auto1.stampa_info()                  # stampa "L'automobile è una Fiat 500"

auto2.stampa_info()                  # stampa "L'automobile è una BMW X3"

print