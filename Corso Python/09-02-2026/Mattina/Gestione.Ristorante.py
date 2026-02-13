"""Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto."""

class Ristorante:
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.piatti = []
        self.prezzi = []

    # --- METODI ---

    def descrivi_ristorante(self):
        print(f"Da {self.nome} la migliore cucina {self.tipo_cucina}!.")

    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    def apri_ristorante(self):
        self.aperto = True
        print(f"{self.nome} è ora aperto!")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"{self.nome} è ora chiuso!")

    def aggiungi_al_menu(self, piatto, prezzo):
        self.piatti.append(piatto)
        self.prezzi.append(prezzo)
        print(f"Aggiunto {piatto} al menu a {prezzo}€")

    def togli_dal_menu(self, piatto):
        if piatto in self.piatti:
            indice = self.piatti.index(piatto)
            self.piatti.pop(indice)
            self.prezzi.pop(indice)
            print(f"{piatto} rimosso dal menu")
        else:
            print("Piatto non trovato nel menu")

    def stampa_menu(self):
        if not self.piatti:
            print("Il menu è vuoto.")
        else:
            print("Menu:")
            for i in range(len(self.piatti)):
                print(f"- {self.piatti[i]}: {self.prezzi[i]}€")

# Creazione oggetto
r1 = Ristorante("Mario il zozzone", "romana")

# Test metodi
r1.descrivi_ristorante()
r1.stato_apertura()

r1.apri_ristorante()
r1.stato_apertura()

r1.aggiungi_al_menu("Zozzona", 17)
r1.aggiungi_al_menu("Carbonara", 15)
r1.aggiungi_al_menu("Matriciana", 12)

r1.stampa_menu()

r1.togli_dal_menu("Carbonara")
r1.stampa_menu()

r1.chiudi_ristorante()
r1.stato_apertura()
