from datetime import datetime

class GestoreAccessi:
    def __init__(self):
        self.__registro_accessi = []
        # Inizializziamo un set per tenere traccia di chi è attualmente in azienda
        self.__presenti_ora = set()

    def registra_movimento(self, persona, tipo_movimento):
        """
        Gestisce sia 'ENTRATA' che 'USCITA'.
        """
        if persona.badge is None:
            print(f"ERRORE: {persona.nome} non ha un badge.")
            return False

        if not persona.badge.attivo:
            print(f"ACCESSO NEGATO: Badge disattivato.")
            return False

        # Logica di controllo stato (Entrata/Uscita)
        if tipo_movimento == "ENTRATA":
            if persona._id_univoco in self.__presenti_ora:
                print(f"{persona.nome} risulta già all'interno!")
                return False
            self.__presenti_ora.add(persona._id_univoco)
        else: # USCITA
            if persona._id_univoco not in self.__presenti_ora:
                print(f"{persona.nome} non può uscire se non è mai entrato!")
                return False
            self.__presenti_ora.remove(persona._id_univoco)

        # Creazione del log
        log = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "persona": f"{persona.nome} {persona.cognome}",
            "movimento": tipo_movimento,
            "ruolo": type(persona).__name__,
            "note": persona.get_permessi()
        }

        self.__registro_accessi.append(log)
        print(f"{tipo_movimento} registrata per {persona.nome}.")
        return True

    def mostra_report_accessi(self):
        print("\n--- LOG MOVIMENTI ODIERNI ---")
        for voce in self.__registro_accessi:
            print(f"[{voce['timestamp']}] {voce['movimento']} - {voce['persona']} ({voce['ruolo']})")
        print(f"Persone attualmente in sede: {len(self.__presenti_ora)}")
        print("--------------------------------\n")