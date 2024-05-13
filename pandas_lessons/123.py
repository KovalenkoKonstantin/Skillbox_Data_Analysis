import pandas as pd
from xlwings import load
from xlwings import view

df = pd.DataFrame(data={'one': [0, 1, 2, 3, 4, 5],
                        'two': [6, 7, 8, 9, 10, 11]})
# открывает дату в excel
view(df)
