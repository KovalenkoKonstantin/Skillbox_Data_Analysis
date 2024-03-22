import pandas as pd
import numpy as np
df = pd.read_csv("WeightLoss.csv")
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000

print(df.info())
print(df.isnull().sum())
df.fillna(0.1, inplace=True)
print(df.head(10))

# Если данных у нас много,
# и при этом потеря строк с пропущенными значениями нас не смущает,
# такие строки можно просто удалить:
df = df.dropna()

print(df.info())
