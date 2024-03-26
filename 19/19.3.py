# Откройте файл Practice1_2.csv
# и загрузите его в DataFrame с помощью библиотеки pandas,
# указав правильный разделитель столбцов и выбрав столбец-индекс.

import pandas as pd

df = pd.read_csv('Practice1_2.csv', sep=';', index_col=0)
print(df.head())
