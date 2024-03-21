import pandas as pd
df = pd.DataFrame([['Anna', 23, 3],
             ['Sam', 36, 12],
             ['Bill', 33, 10],
             ['Moica', 25, 7],
             ['Lisa', 27, 7],
             ['Peter', 32, None]])
df.columns = ['name', 'age', 'expr']

print(df.info())
print(df.shape)
print(df.shape[0])
print(df.shape[1])
print(df.describe())
print(df.columns)

print(df.columns)
aaa = list(df.columns)
aaa[2] = 'experience'
# df.columns = list(df.columns)
# list(df.columns)
# df.columns = ['name', 'age', 'experience']
# df.columns[2] = 'experience'
print(aaa)
print(df.columns)
# df.columns[2] = 'experience'

print(df.index)
