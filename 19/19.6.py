import pandas as pd

df = pd.read_csv('2.3 Практика.csv')
# Скачайте файл Practice2_1.csv,
# загрузите его в DataFrame с помощью библиотеки pandas
# и выведите первые 5 строк этого файла на экран.
print(df.head())
# После этого сохраните этот DataFrame в файл MyPractice2_1.csv,
# при этом укажите в качестве разделителя символ точки с запятой ;
# и задайте столбцу-индексу имя "index".
df.to_csv('MyPractice2_1.csv', sep=';', index_label='index')
df1 = pd.read_csv('MyPractice2_1.csv', sep=';')
print(df1[df1['Date'] > '2012-01-10'].head())
