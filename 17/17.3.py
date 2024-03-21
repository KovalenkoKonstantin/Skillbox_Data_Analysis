import pandas as pd
import numpy as np

df = pd.read_csv("WeightLoss.csv")
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000

print(df.sort_values('total', inplace=True))
print(df.head())

print(df.sort_values('id', inplace=True))
print(df.head())

print(df.sort_values(['total', 'se3']).head())
print(df.sort_values(['total', 'se3'], ascending=False).head(20))
