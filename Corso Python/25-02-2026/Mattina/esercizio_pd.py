import pandas as pd

dati = {
    "Nome": ["Luca", "Maria", "Giulia", "Marco", "Anna", "Paolo", "Sara", "Luca", "Elena", "Davide"],
    "Età": [25, 34, 17, 45, 29, 67, 52, 25, None, 41],
    "Città": ["Roma", "Milano", "Torino", "Roma", "Napoli", "Milano", "Roma", "Roma", "Torino", "Napoli"],
    "Salario": [32000, 45000, 15000, 52000, 38000, 61000, None, 32000, 41000, 47000]
}

df = pd.DataFrame(dati)
print("Dataframe originale:")
print(df)

print(df.head())
print(df.tail())

# Rimozione dei duplicati
df = df.drop_duplicates()

#statistiche descrittive
print(df.describe())

"""# Gestione dei dati mancanti
# Rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df.dropna()"""

# Calcolare la mediana della colonna "Età"
mediana_eta = df["Età"].median()
# Sostituire i valori NaN con la mediana
df["Età"] = df["Età"].fillna(mediana_eta)

# Fare lo stesso per "Salario"
mediana_salario = df["Salario"].median()
df["Salario"] = df["Salario"].fillna(mediana_salario)

# Ordinamento per Età
df = df.sort_values("Età")
print(df)
