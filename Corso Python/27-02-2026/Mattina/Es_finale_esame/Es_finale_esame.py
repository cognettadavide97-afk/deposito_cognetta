import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualizza_dati(nome_file='vendite_grezzo.csv'):
    print(f"--- FASE 1: Importazione dati da {nome_file} ---")
    df = pd.read_csv(nome_file)
    
    print("\n--- VISIONE DEI DATI GREZZI (Prime 10 righe) ---")
    print(df.head(10)) 
    
    print("\n--- INFORMAZIONI SUL DATASET (Tipi e Valori Nulli) ---")
    print(df.info())
    
    print("\n--- STATISTICHE DESCRITTIVE (Per identificare anomalie) ---")
    print(df.describe())
    print("-" * 30)
    
    return df
    
def pulisci_dataset(df_sporco):
    print("\n--- FASE 2: Inizio procedura di pulizia ---")
    
    df = df_sporco.copy()
    righe_iniziali = len(df)
    
    # Pulizia
    df = df.drop_duplicates()
    df = df.dropna(subset=['Prezzo'])
    df = df[df['Quantità'] > 0]
    df['Data'] = pd.to_datetime(df['Data'])
    
    righe_finali = len(df)
    print(f"Pulizia completata. Righe rimosse: {righe_iniziali - righe_finali}")
    return df

def salva_e_analizza(df_pulito, nome_file_output='vendite_pulito.csv'):
    print(f"\n--- FASE 3: Salvataggio e Analisi ---")
    
    # 1. Salvataggio
    df_pulito.to_csv(nome_file_output, index=False)
    print(f"File '{nome_file_output}' salvato con successo.")
    
    # 2. Analisi
    df_pulito['Fatturato'] = df_pulito['Prezzo'] * df_pulito['Quantità']
    
    # --- VISUALIZZAZIONE ---
    
    # Grafico 1: Barre
    vendite_per_prodotto = df_pulito.groupby('Prodotto')['Fatturato'].sum()
    plt.figure(figsize=(10, 5))
    plt.bar(vendite_per_prodotto.index, vendite_per_prodotto.values, color='skyblue')
    plt.title('Fatturato Totale per Prodotto')
    plt.ylabel('Fatturato (€)')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()                
    
    # Grafico 2: Linea
    df_tempo = df_pulito.set_index('Data')
    fatturato_giornaliero = df_tempo['Fatturato'].resample('D').sum()
    
    plt.figure(figsize=(10, 5))
    plt.plot(fatturato_giornaliero.index, fatturato_giornaliero.values, color='green', marker='.')
    plt.title('Andamento Fatturato Giornaliero')
    plt.ylabel('Fatturato (€)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    try:
        # 1. Visualizzazione grezza
        df_grezzo = visualizza_dati()
        
        # 2. Pulizia
        df_pulito = pulisci_dataset(df_grezzo)
        
        # --- VERIFICA DATI PULITI ---
        print("\n--- DATI PULITI (Anteprima) ---")
        print(df_pulito.head(10))
        print(df_pulito.info())
        print("-" * 30)
        
        # 3. Salvataggio e Grafici
        salva_e_analizza(df_pulito)                
        
    except FileNotFoundError:
        print("Errore: Il file 'vendite_grezzo.csv' non esiste.")
        print("Esegui prima il modulo 'generatore_dati.py'.")