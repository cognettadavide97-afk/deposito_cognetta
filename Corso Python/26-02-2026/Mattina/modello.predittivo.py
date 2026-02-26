# ========================================
# MODELLAZIONE PREDITTIVA CHURN
# ========================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# 1️⃣ Carico il dataset
df = pd.read_csv("clienti_telecom.csv")

# 2️⃣ Creo nuova feature: Costo per GB
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"].replace(0, np.nan)

# 3️⃣ Trasformo Churn in variabile numerica
df["Churn_num"] = df["Churn"].map({"No": 0, "Sì": 1})

# 4️⃣ Seleziono le variabili numeriche come feature
X = df[["Età", "Durata_Abonnamento", "Tariffa_Mensile",
        "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]].values
y = df["Churn_num"].values

# 5️⃣ Normalizzo le feature (standardizzazione)
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)

# 6️⃣ Divido dati in training e test (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.3, random_state=42)

# 7️⃣ Creo e alleno il modello di regressione logistica
model = LogisticRegression()
model.fit(X_train, y_train)

# 8️⃣ Predizioni sul test set
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]  # probabilità di churn

# 9️⃣ Valutazione del modello
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print("=== RISULTATI MODELLAZIONE ===")
print("Accuracy:", round(accuracy, 3))
print("AUC:", round(auc, 3))

# 10️⃣ Coefficienti del modello (importanza delle variabili)
feature_names = ["Età", "Durata_Abonnamento", "Tariffa_Mensile",
                 "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]
coef = model.coef_[0]

print("\nCoefficienti del modello:")
for f, c in zip(feature_names, coef):
    print(f"{f}: {round(c, 3)}")