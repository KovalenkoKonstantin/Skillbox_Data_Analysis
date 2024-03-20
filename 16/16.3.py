import pandas as pd
df = pd.DataFrame([['Anna', 23, 3],
             ['Sam', 36, 12],
             ['Bill', 33, 10],
             ['Moica', 25, 7],
             ['Lisa', 27, 7],
             ['Peter', 32, None]])
df.columns = ['name', 'age', 'expr']

print(df['name'])

print(df[['name', 'expr']])

df.index = df['name']
print(df.index)

print(df.loc['Bill', 'age'])
print(df.loc["Sam":"Lisa", "expr"])

print(df.loc['Sam':'Lisa', ['age', 'expr']])
