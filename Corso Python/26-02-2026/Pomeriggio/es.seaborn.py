import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

n_righe=10

df = pd.DataFrame({
    "Altezza": np.random.uniform(1.70, 1.90, size=n_righe).round(2),
    "Età": np.random.randint(20, 40, size=n_righe),
    "Peso": np.random.randint(70, 100, size=n_righe).round(2)
    })

df_norm = df.copy()

# Concetto: Trasformiamo i valori in scala 0-1 usando (x - min) / (max - min)
# Applichiamo l'operazione direttamente sulle colonne scelte.

for colonna in ['Altezza', 'Peso']:
    min_val = df_norm[colonna].min()
    max_val = df_norm[colonna].max()
    df_norm[colonna] = ((df_norm[colonna] - min_val) / (max_val - min_val)).round(2)

# Spiegazione: pandas calcola df['Altezza'].min() una volta sola 
# e lo sottrae a ogni riga della colonna 'Altezza'.

print("--- DATAFRAME ORIGINALE ---")
print(df)
print("\n--- DATAFRAME NORMALIZZATO (Min-Max) ---")
print(df_norm)

# Concetto: Trasformiamo il DataFrame da formato "largo" a "lungo" (tidy data)
# Questo serve a Seaborn per mappare i colori alle diverse variabili in un unico comando.

df_melted = df.melt(value_vars=['Altezza', 'Peso'], var_name='Variabile', value_name='Valore')
df_norm_melted = df_norm.melt(value_vars=['Altezza', 'Peso'], var_name='Variabile', value_name='Valore')

# Spiegazione: .melt() prende le colonne 'Altezza' e 'Peso' e le mette in una sola colonna 'Valore', 
# creando una colonna 'Variabile' che ci dice a cosa appartiene quel numero.

# Concetto: Visualizziamo la distribuzione originale per vedere il "dislivello".

plt.figure(figsize=(10, 5))
sns.kdeplot(data=df_melted, x='Valore', hue='Variabile', fill=True)
plt.title("Distribuzione Originale (Scale Differenti)")
plt.show()

# Spiegazione: Noterai che i picchi sono lontanissimi. 
# L'Altezza è un "punto" stretto vicino allo zero rispetto al Peso che arriva a 100.

# Concetto: Visualizziamo i dati normalizzati per vedere come si sovrappongono ora che sono in scala 0-1.

plt.figure(figsize=(10, 5))
sns.kdeplot(data=df_norm_melted, x='Valore', hue='Variabile', fill=True)
plt.title("Distribuzione Normalizzata (Scala 0-1)")
plt.show()

# Spiegazione: Ora le forme delle distribuzioni sono chiaramente visibili nello stesso grafico. 
# Abbiamo mantenuto la "forma" del dato ma cambiato il "righello" usato per misurarlo.

# Concetto: Utilizziamo plt.subplots per creare una figura con due pannelli (1 riga, 2 colonne).

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Grafico 1: Prima
sns.boxplot(data=df[['Altezza', 'Peso']], ax=axes[0])
axes[0].set_title("Prima (Boxplot)")

# Grafico 2: Dopo
sns.boxplot(data=df_norm[['Altezza', 'Peso']], ax=axes[1])
axes[1].set_title("Dopo Normalizzazione (Boxplot)")

plt.tight_layout()
plt.show()

# Spiegazione: Il Boxplot è utilissimo qui perché mostra chiaramente che dopo la normalizzazione 
# i minimi sono tutti a 0 e i massimi tutti a 1.