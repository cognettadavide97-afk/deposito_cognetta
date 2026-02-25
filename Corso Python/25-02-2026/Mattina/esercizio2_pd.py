"""Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
Caricare i dati in un DataFrame.
Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
Trovare il prodotto più venduto in termini di Quantità.
Identificare la città con il maggior volume di vendite totali.
Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
Visualizzare il numero di vendite per ogni città."""

import pandas as pd
import numpy as np

np.random.seed(42)  # per rendere l'esempio ripetibile

prodotti = ["Laptop", "Smartphone", "Headphones", "Tablet",
    "Chair", "Table", "T-shirt", "Jeans",
    "Sofa", "Bookshelf"]
città = ["Roma", "Milano", "Torino", "Napoli", "Genova", "Bologna", "Firenze", "Palermo"]

# Prezzi fissi per ogni prodotto (in euro)
prezzi_prodotti = {
    "Laptop": 900,
    "Smartphone": 700,
    "Headphones": 80,
    "Tablet": 600,
    "Chair": 60,
    "Table": 300,
    "T-shirt": 25,
    "Jeans": 40,
    "Sofa": 900,
    "Bookshelf": 200
}

n_righe = 20


# Scegli prodotti a caso
prodotti_scelti = np.random.choice(prodotti, n_righe)

df = pd.DataFrame({
    "Prodotto": prodotti_scelti,
    "Quantità": np.random.randint(1, 20, size=n_righe),
    "Prezzo Unitario": [prezzi_prodotti[p] for p in prodotti_scelti],
    "Città": np.random.choice(città, size=n_righe)
})

# Totale vendite
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

print("DataFrame originale:")
print(df)

totale_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum().reset_index()
print("\nTotale vendite per prodotto:")
print(totale_per_prodotto)

quantita_per_prodotto = df.groupby("Prodotto")["Quantità"].sum()
prodotto_piu_venduto = quantita_per_prodotto.idxmax()
quantita_massima = quantita_per_prodotto.max()

print(f"\nProdotto più venduto in termini di quantità: {prodotto_piu_venduto} ({quantita_massima} unità)")

df_vendite_alte = df[df["Totale Vendite"] > 1000]
print("\nVendite superiori a 1000 €:")
print(df_vendite_alte)

df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)
print("\nDataFrame ordinato per Totale Vendite (decrescente):")
print(df_ordinato)

nuovo_dataset = "ordered_data.csv"
df_ordinato.to_csv(nuovo_dataset)

print(nuovo_dataset)