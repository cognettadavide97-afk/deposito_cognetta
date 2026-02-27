import pandas as pd
import numpy as np

#funzione per la creazione di un dataset fittizio
def genera_dataset_sporco(nome_file='vendite_grezzo.csv', n_righe=1000):
    print(f"Generazione di {n_righe} righe di dati...")
    
    np.random.seed(42) # Per riproducibilità

    #creo una libreria con valori generati randomicamente
    data = {
        'ID_Transazione': range(1, n_righe + 1),
        'Data': pd.date_range(start='2023-01-01', periods=n_righe, freq='h'),
        'Prodotto': np.random.choice(['Laptop', 'Mouse', 'Monitor', 'Tastiera'], n_righe),
        'Prezzo': np.random.uniform(10, 1000, n_righe),
        'Quantità': np.random.randint(1, 5, n_righe)
    }

    df = pd.DataFrame(data)

    # Introduzione intenzionale di "sporcizia"
    # 1. Valori nulli casuali nel prezzo (5% dei dati)
    mask_null = np.random.choice(df.index, int(n_righe * 0.05))
    df.loc[mask_null, 'Prezzo'] = np.nan
    
    # 2. Alcune quantità negative (errori di input)
    mask_neg = np.random.choice(df.index, 20)
    df.loc[mask_neg, 'Quantità'] = -1

    # Salvataggio
    df.to_csv(nome_file, index=False)
    print(f"File '{nome_file}' creato con successo.")

if __name__ == "__main__":
    genera_dataset_sporco()