import pandas as pd

df = pd.read_csv('2-1.csv')
print(df.head())
# метод - head
# функция - read.csv
df = pd.read_csv('2-2.csv', sep=';')
print(df.head())
df = pd.read_csv('2-3.csv', index_col='index')
print(df.head())
df = pd.read_csv('2-4.csv', index_col=0)
print(df.head())
