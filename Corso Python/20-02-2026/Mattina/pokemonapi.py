"""Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""

from random import randint
import requests
import json

dex_number = randint(1, 1008) 

def pokemon_info(dex_number):

    #url del sito, inserire id or name
    url_pokedex = f"https://pokeapi.co/api/v2/pokemon/{dex_number}"
    
    try:
        # invio richiesta al sito
        response = requests.get(url_pokedex)
        
        if response.status_code == 200:
            raw_data = response.json()
            print(f"Dati grezzi ricevuti per: {raw_data['name']}")#debug
           
            pokemon_data = {"nome": raw_data["name"],
                            "pokedex_N°": raw_data["id"],
                          "type": [t["type"]["name"] for t in raw_data["types"]]}
                
            return pokemon_data
        
        else:
            print("Errore: Pokémon is MissingNO")
            return None
        
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return None

pokemon_info(dex_number)



"""# Trasforma la risposta in un dizionario (JSON)
    dati = response.json()"""
"""url_encounter = https://pokeapi.co/api/v2/encounter-method/{id or name}/
url_evo = https://pokeapi.co/api/v2/evolution-chain/{id}/"""