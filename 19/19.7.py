# Снова выведите первые 5 строк файла Practice2_1.csv на экран.
# Обратите внимание на столбец AvgTemperature.
# В нем указана температура в градусах Фаренгейта.
# На основе столбца AvgTemperature cоздайте новый столбец
# с названием AvgTemperature_2,
# который будет содержать значения температуры,
# возведенные в квадрат.
# Затем сохраните этот DataFrame в файл MyPractice2_1.csv,
# используя в качестве разделителя запятую.
import pandas as pd

df = pd.read_csv('2.3 Практика_1.csv')
print(df.head())
df = df.assign(AvgTemperature_2=df['AvgTemperature'] * 2)
print(df.head())
df.to_csv('MyPractice2_1.csv', sep=',', index_label=0)
df1 = pd.read_csv('MyPractice2_1.csv', index_col=0)
print(df1.head())
