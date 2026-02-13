"""2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
Descrizione: Chiedi all'utente di inserire un numero N. Il programma dovrebbe stampare la sequenza di Fibonacci fino a N. Ad esempio, se l'utente inserisce 100, 
il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100."""

def fibonacci():
    # Corretto l'input
    n_volte = int(input("Quanti numeri della sequenza vuoi vedere? "))
    
    a = 0
    b = 1
    
    print(f"I primi {n_volte} numeri di Fibonacci:")
    
    for i in range(n_volte):
        print(a, end=" ")
        
        # Usiamo il trucco Python per lo scambio
        a, b = b, a + b
    
    print() # Va a capo alla fine

fibonacci()
        
        

    
    
