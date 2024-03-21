import pandas as pd

df = pd.DataFrame([['Anna', 23, 3],
                   ['Sam', 36, 12],
                   ['Bill', 33, 10],
                   ['Moica', 25, 7],
                   ['Lisa', 27, 7],
                   ['Peter', 32, None]])
df.columns = ['name', 'age', 'expr']
df = df.dropna()

df['age_sq'] = df['age'] ** 2
print(df)
df['no_work'] = df['age'] - df['expr']
print(df)
df['status'] = 'W'  # из одного значения
print(df)
df['gender'] = [0, 1, 1, 0, 0]  # из списка значений
print(df)
