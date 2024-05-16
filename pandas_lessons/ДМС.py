import pandas as pd
import sqlalchemy
import datetime
import pymssql

# настройки
file_name = 'ДМС_ПМ.xlsx'
procedure = 'GetEmployeeRefreshAlt'
company_id = 9

current_year = datetime.datetime.now().strftime('%Y')
current_month = datetime.datetime.now().strftime('%m')

procedure = 'GetVHI'
current_year = 2023

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


result = request(f'execute {procedure} {company_id}, {current_year};')
query = pd.DataFrame(result)


# переношу последний столбец на первое место
df = query[['employee_name'] + [x for x in query.columns if x != 'employee_name']]

# задаю формат последней колонки
df['detachment_date'] = pd.to_datetime(df['detachment_date'], format='%Y-%m-%d')

# замена 1753-01-01 на пустое значение
df = df.replace(to_replace="1753-01-01",
           value="")

# path = 'y:/_Свод документов для РКМ/..............Новое хранение информации/Автоматизация/ДМС/'
path = '//MSK-FS-01/Kvant/'
# запись фрейма в excel
with pd.ExcelWriter(path + file_name, engine="xlsxwriter", mode='w') as writer:
    df.to_excel(writer, sheet_name='ДМС', index=False)

    #Auto adjust columns
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['ДМС'].set_column(col_idx, col_idx, column_width)

# pyinstaller --noconsole --onefile ДМС.py
# auto-py-to-exe

