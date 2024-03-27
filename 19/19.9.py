# Скачайте файл Practice3_1.csv,
# загрузите его в DataFrame
# с помощью библиотеки pandas
# и выведите первые 5 строк этого файла на экран.
# Определите, какой формат дат используется в столбце Date.
# После этого загрузите файл Practice3_1.csv в DataFrame снова,
# использовав параметры parse_dates и dayfirst.
import pandas as pd

df = pd.read_csv('2.4 Practice3_1.csv', parse_dates=['Date'], dayfirst=True)
print(df[df['Date'] > '2012-02-15'].head())
