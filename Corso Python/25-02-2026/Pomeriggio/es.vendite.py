"""Esercizio 1: Analisi di Vendite Fittizie
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.
Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.
Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto."""


import pandas as pd
import numpy as np

np.random.seed(42) 


# 1) Creiamo i dati in modo casuale e li carichiamo in un DataFrame
np.random.seed(42)  # per rendere l'esempio ripetibile

data = range(1,31)
città = ["Roma", "Milano", "Torino", "Napoli"]
prodotti_prezzi = {
    "Smartphone": 799,
    "Laptop": 1099,
    "Tablet": 499,
    "Smartwatch": 299,
    "Cuffie wireless": 149,
    "Auricolari Bluetooth": 99,
    "Monitor": 249,
    "Tastiera meccanica": 129,
    "Mouse wireless": 59,
    "Smart TV": 899,
    "Console di gioco": 549,
    "Webcam": 79,
}

n_righe =  30

quantità = np.random.randint(1, 6, size=n_righe)

df = pd.DataFrame({
    "Data": np.random.choice(data, size=n_righe),
    "Prodotto": np.random.choice(list(prodotti_prezzi.keys()), size=n_righe),
    "Città": np.random.choice(città, size=n_righe)
    })

df["Vendite"] = [prodotti_prezzi[df["Prodotto"].iloc[i]] * quantità[i] for i in range(n_righe)]

print("\n Dataframe originale:")
print(df)

print("\n vendite medie per città:")
# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print(pivot_df)

print("\n vendite totali")
grouped_df = df.groupby('Prodotto')['Vendite'].sum().reset_index()
print(grouped_df)

nuovo_dataset = "sale_data.csv"
grouped_df.to_csv(nuovo_dataset)

print(nuovo_dataset)