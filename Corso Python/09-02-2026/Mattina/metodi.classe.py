class Calcolatrice:

    @staticmethod

    def somma(a, b):

        return a + b

# Uso del metodo statico senza creare un'istanza

risultato = Calcolatrice.somma(5, 3)

print(risultato)  

# Output: 8

#serve quando la classe deve fare qualcosa che è un metodo indipendente (tipo duplicare)

"""-----------------------------------------------------------------------------
class method lavora dentro la classe. serve a lavorare DENTRO la classe. Compie azioni solo INTERNE """

class Contatore:

    numero_istanze = 0  # Attributo di classe

    def __init__(self):

        Contatore.numero_istanze += 1

    @classmethod

    def mostra_numero_istanze(cls):

        print(f"Sono state create {cls.numero_istanze} istanze.")

# Creazione di alcune istanze

c1 = Contatore()

c2 = Contatore()

Contatore.mostra_numero_istanze()  

# Output: Sono state create 2 istanze.

"""--------------------------------------------------------------------------------------
"""