# Откройте файл Practice1_1.csv,
# загрузите его в DataFrame с помощью библиотеки pandas
# и выведите первые 5 строк этого файла на экран.
# Выведите на экран название предпоследнего столбца этого файла.
# Обратите внимание,
# что при загрузке файла вам может потребоваться
# явно указать разделитель столбцов.

import pandas as pd

df = pd.read_csv('Practice1_1.csv')
print(df.head())
new_list = list(df.columns.values)
x = len(new_list)-2
print(new_list[x])
print(x)
print(df.columns[-2])
