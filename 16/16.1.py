import pandas as pd

df = pd.DataFrame([['Anna', 23, 3],
             ['Sam', 36, 12],
             ['Bill', 33, 10],
             ['Moica', 25, 7],
             ['Lisa', 27, 7],
             ['Peter', 32, None]])
print(df)
print(type(df))

print(df[0])
print(type(df[0]))
