# Откройте файл Practice1_3.csv,
# загрузите его в DataFrame с помощью библиотеки pandas
# и выведите первые 5 строк этого файла на экран.
# Выведите на экран все записи,
# в которых значение температуры превышает 30 градусов.
# Обратите внимание,
# что вам может потребоваться явно указать разделитель столбцов.

import pandas as pd

df = pd.read_csv('Practice1_3.csv')
print(df.head())
df = df[df['AvgTemperature'] > 30]
print(df.head())
print(list(df.columns)[4])
df = df[df[list(df.columns)[4]] > 32]
print(df.head())
