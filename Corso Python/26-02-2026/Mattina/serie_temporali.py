
import pandas as pd
import numpy as np

date_range = pd.date_range(start='2021-01-01', periods=10, freq='ME')

df = pd.DataFrame({'value': range(10)}, index=date_range)

df_resampled = df.resample('ME').mean()

print(df_resampled)


# esempio: colonna “date” in stringhe → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(df['date'])

"""DataFrame.resample()

Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati,
specificando l’intervallo desiderato (‘D’=day, ‘M’=month, ‘H’=hour, …)."""

# partendo da un DataFrame con indice DatetimeIndex:
df_daily = df.resample('D').mean()      # media giornaliera
df_monthly = df.resample('ME').sum()     # somma mensile