# На основе столбца "Date"
# создайте новый столбец "Month",
# который будет содержать номер месяца (от 1 до 12),
# соответствующего дате в каждой строке.
# Затем сохраните этот DataFrame в файл MyPractice3_1.csv,
# используя в качестве разделителя точку с запятой ;.
import pandas as pd

df = pd.read_csv('2.4 Practice3_1.csv', parse_dates=['Date'], dayfirst=True)
print(df[df['Date'] > '2012-02-15'].head())
df['Month'] = df['Date'].dt.month
print(df.head())
# https://pandas.pydata.org/pandas-docs/stable/reference/series.html#datetimelike-properties
df.to_csv('MyPractice3_1.csv', sep=';')
df1 = pd.read_csv('MyPractice3_1.csv', sep=';', index_col=0)
print(df1)
