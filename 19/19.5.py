import pandas as pd

df = pd.read_csv('2-1.csv')
print(df.head())
df.to_csv('result.csv', index_label='index')

df = pd.read_csv('Practice1_3.csv')
print(df.head())
