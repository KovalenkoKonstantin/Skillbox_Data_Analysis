import pandas as pd
import numpy as np
df = pd.read_csv("WeightLoss.csv")
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000

df.groupby('group')

print(list(df.groupby('group'))[0])

print(df.groupby('group').agg('sum'))  # название функции - в кавычках
print(df.groupby('group').agg('mean'))
print(df.groupby('group').agg(['min', 'max', 'mean']))
