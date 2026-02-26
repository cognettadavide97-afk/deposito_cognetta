
import pandas as pd

# esempio: colonna “date” in stringhe → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(df['date'])

"""DataFrame.resample()

Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati,
specificando l’intervallo desiderato (‘D’=day, ‘M’=month, ‘H’=hour, …)."""

# partendo da un DataFrame con indice DatetimeIndex:
df_daily = df.resample('D').mean()      # media giornaliera
df_monthly = df.resample('M').sum()     # somma mensile

