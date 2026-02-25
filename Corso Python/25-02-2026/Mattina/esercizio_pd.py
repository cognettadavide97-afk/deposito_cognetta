import pandas as pd

dati = {
    "Nome": ["Luca", "Maria", "Giulia", "Marco", "Anna", "Paolo", "Sara", "Luca", "Elena", "Davide"],
    "Età": [25, 34, 17, 45, 29, 67, 52, 25, None, 41],
    "Città": ["Roma", "Milano", "Torino", "Roma", "Napoli", "Milano", "Roma", "Roma", "Torino", "Napoli"],
    "Salario": [32000, 45000, 15000, 52000, 38000, 61000, None, 32000, 41000, 47000]
}

df = pd.DataFrame(dati)
print("\n=== Dataframe originale ===")
print(df)

print("\n=== Prime 5 righe ===")
print(df.head())

print("\n=== Ultime 5 righe ===")
print(df.tail())

#tipi di dato di ogni colonna
print("\n=== Tipi di dato ===")
print(df.dtypes)

print("\n=== Media, Mediana, Dev. Standard + Extra ===")
print(df.describe())

print("\n=== Duplicati ===")
#Identificare e rimuovere eventuali duplicati
duplicati_prima = df.duplicated().sum()
print("Duplicati trovati:", duplicati_prima)

#rimozione dei duplicati
df = df.drop_duplicates()

duplicati_dopo = df.duplicated().sum()
print("Duplicati dopo la rimozione:", duplicati_dopo)

# Calcolare la mediana della colonna "Età"
mediana_eta = df["Età"].median()
# Sostituire i valori NaN con la mediana
df["Età"] = df["Età"].fillna(mediana_eta)

# Fare lo stesso per "Salario"
mediana_salario = df["Salario"].median()
df["Salario"] = df["Salario"].fillna(mediana_salario)

# 7) Aggiungere una colonna "Categoria Età"
# 0-18: Giovane, 19-65: Adulto, oltre 65: Senior
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"
    
df["Categoria Età"] = df["Età"].apply(categoria_eta)

print("\n=== DataFrame con colonna 'Categoria Età' ===")

print(df)

print("\n" + "-"*60 + "\n")

# Ordinamento per Età
df = df.sort_values("Età")
print(df)

nuovo_dataset = "cleaned_data.csv"
df.to_csv(nuovo_dataset)

print(nuovo_dataset)