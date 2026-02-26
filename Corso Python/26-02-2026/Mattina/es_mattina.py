import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("clienti_telecom.csv")
print(df)

#struttura del dataset
print("\nINFO DATASET")
df.info()

#statistiche descrittive
print("\nSTATISTICHE")
print(df.describe())

#distribuzione churn (tasso di abbandono)
print("\nDISTRIBUZIONE CHURN (%)")
print(df["Churn"].value_counts(normalize=True) * 100)

df_grouped = df.groupby("Churn").mean(numeric_only=True)
print("\nMedie delle variabili per Churn:")
print(df_grouped)

"""df_grouped2 = df.groupby("Tariffa_Mensile")["Dati_Consumati"].mean().reset_index()
print("\nMedie tra tariffa e dati consumati:")
print(df_grouped2)"""

# Attenzione: se Dati_Consumati = 0, evito divisione per zero
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"].replace(0, np.nan)
"""print(df["Costo_per_GB"])"""

#Trasformo Churn in numerico
df["Churn_num"] = df["Churn"].map({"No": 0, "Sì": 1})

#raggruppo nuovamente tutto quanto per avere i valori di churn in int
numeriche = ["Età", "Durata_Abonnamento", "Tariffa_Mensile", 
             "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB", "Churn_num"]

"""corr_matrix = df[numeriche].corr().sort_values("Costo_per_GB")
print(corr_matrix)"""

print(df[df["Churn"] == "Sì"]["Servizio_Clienti_Contatti"].describe())
print(df[df["Churn"] == "No"]["Servizio_Clienti_Contatti"].describe())

X = df[["Età", "Durata_Abonnamento", "Tariffa_Mensile",
        "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]].values
y = df["Churn_num"].values