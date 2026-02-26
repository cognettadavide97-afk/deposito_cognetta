import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(10) #seed 10 per andamento più crescente

n_righe = 30

# Qui diciamo a Python: "Generami 30 variazioni"
variazioni = np.random.uniform(-1.5, 1.5, size=n_righe)

# np.cumsum (Cumulative Sum) somma i valori man mano:
# Se variazioni è [1, -0.5, 2], cumsum diventa [1, 0.5, 2.5]
andamento = np.cumsum(variazioni)

# Aggiungiamo una base (es. 12 gradi) per traslare tutto il grafico
temperature_vere = andamento + 12

"""temperature = range(10,15)"""

"""df = pd.DataFrame({ "temperature": np.random.choice(temperature_vere, size=n_righe)})"""
df = pd.DataFrame({"temperature": temperature_vere})

#temp max, min, media e mediana nei 30 gg
temp_max = df['temperature'].max()
temp_min = df['temperature'].min()
temp_media = df['temperature'].mean()
temp_mediana = df['temperature'].median()

#print per la visualizzazione pre-grafico
print(f"Temperatura Massima: {temp_max}°C")
print(f"Temperatura Minima: {temp_min}°C")
print(f"Temperatura Media: {temp_media:.2f}°C")
print(f"Mediana delle Temperature: {temp_mediana}°C")

"""#plt.figure(figsize=(width, height))
plt.figure() #default
#bins sono gli intervalli, color il colore dei punti degli intervalli e edgecolor il contorno
plt.hist(df['temperature'], bins=7, color='skyblue', edgecolor='black')
plt.grid(axis='y', alpha=0.3)
plt.title('Istogramma')
plt.xlabel('Gradi in Celsius')
plt.ylabel('Numero di giorni')
plt.show()"""

plt.figure(figsize=(10, 5))
plt.plot(df['temperature'], 
         marker='o',
         color='slategray',     # Colore della linea (es. 'red', 'skyblue', '#FF5733')
         linestyle='-',         # Tipo di linea: '--' tratteggiata, ':' punteggiata, '-' continua
         markersize=4,
         linewidth=1.5,          # Spessore della linea
         markerfacecolor='black',# Colore interno del punto
         markeredgewidth=2,      # Spessore del bordo del punto
         label='Temp. Febbraio')     # Nome per la legenda) # Usa indice 0-

# Riempiamo lo sfondo sotto la linea (il tocco verosimile)
plt.fill_between(range(30), df['temperature'], color='lightgray', alpha=0.4)

# Diciamo: "Sui posti 0-29, scrivi i numeri 1-30"
plt.xticks(ticks=range(30), labels=range(1, 31))
# Definiamo i tick per l'asse Y: solo numeri interi da 10 a 15
plt.yticks(range(int(df['temperature'].min()), int(df['temperature'].max()) + 2))
"""plt.yticks(range(10, 16)) # In questo modo, spariranno i vari 10.5, 11.0, 11.5 ecc."""
plt.ylim(temp_min - 1, temp_max + 1)

plt.title('Silent Hill: Andamento Temperature')
plt.grid(axis='y', alpha=0.2) # Griglia leggera solo orizzontale
plt.show()