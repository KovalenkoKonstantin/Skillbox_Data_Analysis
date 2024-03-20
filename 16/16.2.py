import pandas as pd

df = pd.DataFrame([['Anna', 23, 3],
             ['Sam', 36, 12],
             ['Bill', 33, 10],
             ['Moica', 25, 7],
             ['Lisa', 27, 7],
             ['Peter', 32, None]])

df.columns = ['name', 'age', 'expr']

print(df)

print(df.iloc[1, 2])

print(df.iloc[1:3, 1])

print(df.iloc[:, 0])

print(df.iloc[1:3, :])

print(df[0:2])
