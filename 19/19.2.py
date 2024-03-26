import pandas as pd

df = pd.read_csv('Practice1_1.csv')
print(df.head())
new_list = list(df.columns.values)
x = len(new_list)-2
print(new_list[x])
# print(x)
