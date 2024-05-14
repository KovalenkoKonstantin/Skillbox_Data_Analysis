import pandas as pd
import sqlalchemy
import datetime
from tkinter import filedialog as fd
from openpyxl import Workbook
import pymssql

# настройки
file_name = 'award_calculation.xlsx'
procedure = 'GetSalaryListShchepetovaAlt'
company_id = 9

current_year = datetime.datetime.now().strftime('%Y')
current_month = datetime.datetime.now().strftime('%m')

# получение данных из excel
name = fd.askopenfilename()
path = '/'.join(name.split('/')[:-1]) + '/'

data = pd.read_excel(name, dtype={'Таб. номер': str})
# data
# data['%'] = data['%'].fillna(0)
data = data.dropna(subset=['%'])
# data
data['employee_name'] = data['Имя'].apply(lambda x: x.split()[0]) + ' ' + data['Имя'].apply(
    lambda x: x.split()[1]) + ' ' + data[
                            'Имя'].apply(lambda x: x.split()[2])

# data.to_excel(r'D:/123.xlsx', index=True)

final_data = data[['employee_name', 'Таб. номер', '%']]
final_data.index.rename('index', inplace= True )
# final_data

# получение данных из sql
def request(request):
    version = 'mssql'
    driver = 'pymssql'
    user = 'rkm_ro'
    password = 'ip%U1PO7C$Zb'
    server = 'msk-sql-02'
    data_base = 'RKM'
    # request = 'exec GetEmployeeRefresh 9'

    conn = f'{version}+{driver}://{user}:{password}@{server}/{data_base}?charset=utf8'

    engine = sqlalchemy.create_engine(conn)  # создание отдельного подключения к БД
    connect = engine.connect()  # создаётся объект подключения к БД
    df = pd.read_sql(f"{request}", connect)
    return df


result = request(f'execute {procedure} {current_month}, {current_year}, {company_id};')
query = pd.DataFrame(result)
# query

# объединение данных excel с sql
new_data = final_data.merge(query, on='employee_name', how='left')
new_data = new_data[['employee_name', '%', 'Таб. номер', 'salary_budget_ammount']]
# new_data

# добавление вычисляемой колонки
new_data['prize'] = new_data.apply(lambda row: round(row['%'] * row['salary_budget_ammount'] * 0.45 / 100, 0), axis=1)
new_data.drop(new_data.loc[new_data['%'] == 0].index, inplace=True)
new_data.index.rename('index', inplace= True )
# new_data

# df_pivot_table = pd.pivot_table(new_data,
#                                 index='employee_name',
#                                 values=['%', 'Таб. номер', 'salary_budget_ammount', 'prize'])
# df_pivot_table

# запись фрейма в excel
with pd.ExcelWriter(path + file_name, engine="xlsxwriter", mode='w') as writer:
    new_data.to_excel(writer, sheet_name='Премии', index=False)

    #Auto adjust columns
    for column in new_data:
        column_width = max(new_data[column].astype(str).map(len).max(), len(column))
        col_idx = new_data.columns.get_loc(column)
        writer.sheets['Премии'].set_column(col_idx, col_idx, column_width)

# writer.close()

# new_data.to_excel(
#     path + file_name,
#     index=False, sheet_name='Премии')

# pyinstaller --noconsole --onefile main.py
# auto-py-to-exe
