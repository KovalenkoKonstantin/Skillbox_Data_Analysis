import pandas as pd

# df = pd.read_excel('2.5 5-1.xlsx')
# print(df.head())

# df = pd.read_excel('2.5 5-2.xlsx')
# print(df.head())
df = pd.read_excel('2.5 5-2.xlsx', sheet_name='Sheet2')
# print(df.head(30))
df = pd.read_excel('2.5 5-2.xlsx', sheet_name='Sheet2', parse_dates=['Date'])
# print(df.head(30))
df.to_excel('result.xlsx', index_label='index')
df1 = pd.read_excel('result.xlsx', index_col='index')
print(df1.head())
