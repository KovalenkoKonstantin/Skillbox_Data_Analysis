import pandas as pd
import numpy as np  # тоже пригодится

df = pd.read_csv("WeightLoss.csv")
# pd.read_excel()
print(df.head())
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000
print(df.head())
df['total_gr'].apply(np.log)  # применяем log из numpy
df['avloss'] = df.loc[:, 'w1':'w3'].apply(np.mean, axis=1)
print(df.head())
print(df.loc[:, 'w1':'w3'].apply(np.mean, axis=0))
f = lambda x: x.max() - x.min()
df['wrange'] = df.loc[:, 'w1':'w3'].apply(f, axis=1)
print(df.head())

import pandas as pd
import numpy as np

# создадим маленький датафрейм
ages = pd.DataFrame({'age':[np.nan, 25, np.nan, 29],
                   'income':[20000, np.nan, 26000, 30000],
                   'children':[2, 1, 3, np.nan]})
ages
# заполним всё нулями
ages.fillna(0)
print(ages)
print(ages.fillna(0))

# вспомним, как считается среднее по столбцам
ages.mean()
# подставим .mean()
# могли бы взять .median()
print(ages.fillna(ages.mean()))
# заполним столбец age средним
# столбец income – медианой
# столбец children – нулями

print(ages.fillna({'age': ages['age'].mean(),
             'income': ages['income'].median(),
             'children': 0}))
# вместо NaN в строке 2 стоит значение из строки 1 (age)
# вместо NaN в строке 1 стоит значение из строки 0 (income)
# вместо NaN в строке 3 стоит значение из строки 2 (children)

print(ages)
print(ages.fillna(method='ffill'))
print(ages.fillna(method='bfill'))
