"""Esercizio 1 (Facile):
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano. Devono essere ripetibili"""

class Punto():
    
    def __init__(self, x=0, y=0):
        #assegno i valori iniziali della istanza
        self.x = x
        self.y = y
        
    def muovi (self, dx, dy):
        #sommiamo lo spostamento alle coordinate attuali
        self.x += dx
        self.y += dy
        
    def distanza_da_origine(self):
        # Applichiamo Pitagora: radice quadrata di (x² + y²)
        distanza = ((self.x**2 + self.y**2)**0.5)
        return distanza
    
p1 =  Punto(3, 4)
print(f"distanza inzile {p1.distanza_da_origine()}")
        
while True:
    
    dist = p1.distanza_da_origine()
    print(f"La nuova distanza è: {dist}")
    
    dx_spostamento = int(input("inserisci il valore di spostamento per dx: "))
    dy_spostamento = int(input("inserisci il valore di spostamento per dy: "))
    p1.muovi(dx_spostamento, dy_spostamento) = Punto(3, 4)
    print(f"Nuove coordinate: ({p1.x}, {p1.y})") # Output: (5, 6)

"""Esercizio 2 (Facile):
Crea una classe chiamata Libro. Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo 
"Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine. deve essere ripetibile"""

"""EXTRA: Andare a gestire nel primo esercizio X punti 
che sono X oggetti che deve definire tutti e stampare tutti assieme."""