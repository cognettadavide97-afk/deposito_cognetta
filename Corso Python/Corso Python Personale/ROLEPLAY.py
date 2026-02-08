print ("TITOLO: --- WELCOME TO AGARTHA ---")

#obiettivo guidare una carovana attraverso tre tappe (Bosco Tetro, Picchi Gelidi, Deserto di Sale)
#per consegnare un carico alla Capitale

def viaggio():
    inventario = ["Cibo", "Oro", "Manufatto Oscuro"]
    tappe = ("Bosco Tetro", "Deserto di Sale", "Picchi Gelidi")
    
    print(f"Benvenuto, Messere. Il viaggio verso la Capitale ha inizio.")

    for tappa in tappe:
        print(f"\n--- Sei entrato in: {tappa} ---")
        
        attivo = True
        while attivo:
            scelta = input("Vuoi (P)roseguire, (R)iposare o (I)nventario? ").upper()
            
            match scelta:
                case "P":
                    print("Si riparte!")
                    # Qui inserisci logica per eventi e consumi
                    attivo = False 
                case "R":
                    # Usa continue o logica per saltare il turno
                    print("Vi riposate sotto le stelle.")
                case "I":
                    # Mostra inventario con f-string
                    pass # Da implementare
                case _:
                    print("Comando non valido.")

    print("Sei arrivato a destinazione!")

# Avvia il gioco
# viaggio()