import pandas as pd
df = pd.DataFrame([['Anna', 23, 3],
             ['Sam', 36, 12],
             ['Bill', 33, 10],
             ['Moica', 25, 7],
             ['Lisa', 27, 7],
             ['Peter', 32, None]])
df.columns = ['name', 'age', 'expr']

print(df)
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))
df = df.dropna()
print(df)
print(df[df['age'] > 30])
print(df[(df['age'] > 30) & (df['expr'] > 7)])  # не забываем круглые скобки
print(df[(df['age'] > 35) | (df['age'] < 25)])