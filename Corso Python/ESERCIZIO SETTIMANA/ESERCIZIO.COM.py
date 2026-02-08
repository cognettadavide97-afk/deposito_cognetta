#Scrivere un programma che analizzi una lista di prodotti
#aggiorni le quantità in base agli ordini e stampi un report finale utilizzando diverse strutture dati.

# 1. PREPARAZIONE DELLE BASI E FUNZIONI
carrello = []

def acquisto(prodotto, quantita):
    carrello.append((prodotto, quantita))
    return carrello

catalogo_giochi = ("Deltarune", "Pokémon Scarlatto", 
                   "Bloodborne", "Zelda: BOTW", 
                   "AC: New Horizon", "Cyberpunk 2077")
prezzo_giochi = (9.99, 59.99, 39.99, 59.99, 59.99, 69.99)

# 2. CICLO DI ACQUISTO (IL NEGOZIO)
while True:
    print("\n--- 🎮 GAME SHOP (Versione Sicura) ---")
    for i in range(len(catalogo_giochi)):
        print(f"{i + 1}. {catalogo_giochi[i]} - {prezzo_giochi[i]:.2f}€")

    try:
        scelta = int(input("\nScegli il numero del gioco (o 0 per uscire): "))
        
        if scelta == 0: # Uscita rapida
            break
            
        if 1 <= scelta <= len(catalogo_giochi):
            gioco_scelto = catalogo_giochi[scelta - 1]
            qta = int(input(f"Quante copie di {gioco_scelto} vuoi? "))
            
            if qta <= 0:
                print("❌ Devi inserire almeno 1 copia!")
                continue
                
            acquisto(gioco_scelto, qta)
            print(f"✅ {gioco_scelto} aggiunto! Carrello: {len(carrello)} articoli.")
            
        else:
            print(f"❌ Errore: Scegli un numero tra 1 e {len(catalogo_giochi)}!")
            continue

    except ValueError:
        print("❌ Errore: Devi inserire un NUMERO!")
        continue

    # Validazione rigorosa SI/NO
    while True:
        continua = input("\nVuoi comprare altro? (s/n): ").lower().strip()
        if continua in ('s', 'n'):
            break
        print("❌ Risposta non valida! Usa 's' o 'n'.")

    if continua == 'n':
        break

# 3. ELABORAZIONE DATI (CALCOLO CONTO)
# Spostato qui così sappiamo quanto far pagare prima di chiedere il metodo
if carrello:
    totale_finale = 0
    prezzi_per_splat = []

    print("\n" + "="*30)
    print("DETTAGLIO COSTI:")
    for gioco, qta in carrello:
        indice = catalogo_giochi.index(gioco)
        prezzo_unitario = prezzo_giochi[indice]
        subtotale = prezzo_unitario * qta
        totale_finale += subtotale
        prezzi_per_splat.append(subtotale)
        print(f"• {gioco} x{qta}: {subtotale:.2f}€")
    
    print(f"TOTALE DA PAGARE: {totale_finale:.2f}€")
    #print("Dettaglio subtotali (Splat):", *prezzi_per_splat)
    print("="*30)

    # 4. FASE DI PAGAMENTO (MATCH-CASE)
    print("\nScegli il metodo di pagamento:")
    metodo = input("1. Carta | 2. Paypal | 3. Satispay: ")
    
    match metodo:
        case "1":
            msg_pagamento = "Pagamento con Carta effettuato!"
        case "2":
            msg_pagamento = "Reindirizzamento a PayPal..."
        case "3":
            msg_pagamento = "Pagherai tramite Satispay."
        case _:
            msg_pagamento = "Metodo non valido, selezionato ritiro in negozio."
    
    print(f"\nStato: {msg_pagamento}")

    # 5. RICEVUTA FINALE
    print("\n--- 🧾 RICEVUTA FINALE ---")
    for g, q in carrello:
        print(f"- {g}: {q} pz")
    print("\nGrazie per il tuo acquisto! A presto.")

else:
    print("\nCarrello vuoto. Arrivederci!")