# ISO 8601
import pandas as pd

df = pd.read_csv('2.3 Практика_1.csv')
print(df.head(30))

df = pd.read_csv('2.3 Практика_1.csv', parse_dates=['Date'], dayfirst=False)
print(df.head(30))

df['Day_of_week'] = df['Date'].dt.day_name()
print(df.head())
# https://pandas.pydata.org/pandas-docs/stable/reference/series.html#datetimelike-properties
