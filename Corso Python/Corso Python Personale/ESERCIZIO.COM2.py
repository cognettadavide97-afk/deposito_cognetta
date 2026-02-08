#1 def: Creiamo una funzione per aggiungere prodotti, che controlli se il dato inserito è valido. 
#crep una funzione, dove inserisco dei "parametri" o "nomi di variabile" che dir si voglia al suo interno
#NOTA: non posso inserisci un comando, come input
# 1. PREPARAZIONE DELLE BASI
carrello = []

def acquisto(prodotto, quantita):
    carrello.append((prodotto, quantita))
    return carrello

catalogo_giochi = ("Deltarune", "Pokémon Scarlatto", 
                   "Bloodborne", "Zelda: BOTW", 
                   "AC: New Horizon", "Cyberpunk 2077")
prezzo_giochi = (9.99, 59.99, 39.99, 59.99, 59.99, 69.99)

while True:
    print("\n--- 🎮 GAME SHOP (Versione Sicura) ---")
    for i in range(len(catalogo_giochi)):
        print(f"{i + 1}. {catalogo_giochi[i]} - {prezzo_giochi[i]: .2f}") #2f mi permette di mostrare solo 2 decimali

    # --- BLOCCO DI SICUREZZA ---
    try:
        scelta = int(input("\nScegli il numero del gioco: "))
        
        # Controllo se il numero esiste nel catalogo
        if 1 <= scelta <= len(catalogo_giochi):
            gioco_scelto = catalogo_giochi[scelta - 1]
            
            qta = int(input(f"Quante copie di {gioco_scelto} vuoi? ")) #se inserisco 0 mi restituisce cp2077
            if qta <= 0:
                print("❌ Devi inserire almeno 1 copia!")
                continue # Ricomincia il ciclo da capo
                
            acquisto(gioco_scelto, qta)
            print(f"✅ {gioco_scelto} aggiunto! Al momento hai {len(carrello)} articoli.")

            
        else:
            print(f"❌ Errore: Scegli un numero tra 1 e {len(catalogo_giochi)}!")
            continue # Salta il resto e ricomincia il ciclo

    except ValueError:
        print("❌ Errore: Devi inserire un NUMERO, non una lettera!")
        continue
    # ---------------------------

    while True:
        continua = input("\nVuoi comprare altro? (s/n): ").lower().strip()
        if continua == 's' or continua == 'n':
            break # Esce da questo piccolo ciclo perché la risposta è valida
        print("❌ Risposta non valida! Scrivi 's' per sì o 'n' per no.")

    if continua == 'n':
        break # Esce dal ciclo principale del negozio
        
totale_finale = 0
prezzi_per_splat = [] # Creiamo una lista per usare lo splat dopo
print(prezzi_per_splat)

print("Scegli il metodo di pagamento: ")  
metodo = input("1. Carta | 2. Paypal | 3. Satispay")  
match metodo:
    case "1":
        msg_pagamento = "Pagamento con Carta effettuato!"
    case "2":
        msg_pagamento = "Reindirizzamento a PayPal..."
    case "3":
        msg_pagamento = "Pagherai alla consegna."
    case _:
        msg_pagamento = "Metodo non valido, selezionato ritiro in negozio."

for gioco, qta in carrello:
    # Troviamo l'indice del gioco per sapere quanto costa
    indice = catalogo_giochi.index(gioco)
    prezzo_unitario = prezzo_giochi[indice]
    subtotale = prezzo_unitario * qta
    totale_finale += subtotale
    prezzi_per_splat.append(subtotale)
    print(f"• {gioco} x{qta}: {subtotale:.2f}€")

print(f"\nTOTALE DA PAGARE: {totale_finale:.2f}€")
# Esempio Splat:
print("Dettaglio subtotali spacchettati:", *prezzi_per_splat)

print("\n--- RICEVUTA FINALE ---")
for g, q in carrello:
    print(f"- {g}: {q} pz")

# 4. RIEPILOGO FINALE (La Cassa)
print("\n" + "="*30) #separatore di testo
print("IL TUO CARRELLO FINALE:")
for gioco, pezzi in carrello:
    print(f"• {gioco}: {pezzi} copie")
print("="*30) #separatore 
print("Grazie per il tuo acquisto! A presto.")

