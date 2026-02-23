import requests

# --- 1. GEOCODING (Trova le coordinate della città) ---
citta_utente = input("Inserisci il nome della città: ").strip().capitalize()
url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={citta_utente}&count=1&language=it&format=json"

risposta_geo = requests.get(url_geo).json()

if "results" not in risposta_geo:
    print("Città non trovata. Riprova.")
    exit()

# Estraiamo i dati della città
risultato = risposta_geo["results"][0]
lat = risultato["latitude"]
lon = risultato["longitude"]
nome_citta = risultato["name"]

# --- 2. PREFERENZE UTENTE ---
giorni = input("Quanti giorni vuoi vedere? (1, 3, 7): ")
vuoi_vento = input("Vuoi vedere la velocità del vento? (s/n): ").lower()
vuoi_pioggia = input("Vuoi vedere le precipitazioni? (s/n): ").lower()

# --- 3. COSTRUZIONE URL METEO (Dinamico) ---
# Partiamo con i parametri base obbligatori
url_meteo = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"

# Aggiungiamo dati extra con la VIRGOLA all'interno del parametro 'daily'
if vuoi_vento == 's':
    url_meteo += ",windspeed_10m_max"

if vuoi_pioggia == 's':
    url_meteo += ",precipitation_sum"

# Aggiungiamo i parametri di configurazione finali con la '&'
url_meteo += f"&forecast_days={giorni}&timezone=auto"

# --- 4. RICHIESTA DATI METEO ---
risposta_meteo = requests.get(url_meteo).json()
previsioni = risposta_meteo["daily"]

# --- 5. OUTPUT FINALE (Il ciclo for sistemato) ---
print(f"\n" + "="*40)
print(f"PREVISIONI METEO PER: {nome_citta}")
print("="*40)

for i in range(len(previsioni["time"])):
    giorno = previsioni["time"][i]
    t_max = previsioni["temperature_2m_max"][i]
    t_min = previsioni["temperature_2m_min"][i]
    
    # Prepariamo la stringa base
    output = f"Data: {giorno} | Temp: {t_min}° / {t_max}°C"
    
    # Aggiungiamo il vento solo se presente nel JSON
    if "windspeed_10m_max" in previsioni:
        v_vento = previsioni["windspeed_10m_max"][i]
        output += f" | Vento: {v_vento} km/h"
        
    # Aggiungiamo la pioggia solo se presente nel JSON
    if "precipitation_sum" in previsioni:
        v_pioggia = previsioni["precipitation_sum"][i]
        output += f" | Pioggia: {v_pioggia} mm"
        
    print(output)

print("="*40)