import sqlalchemy
import pandas as pd
import psycopg2
from sqlalchemy.ext.asyncio import create_async_engine

# conn = 'postgresql+psycopg2://readonly:6hajV34RTQfmxhS@dsstudents.skillbox.ru:5432/db_ds_students'
# conn = 'jdbc:sqlserver://msk-sql-02;database=RKM'
# conn = 'mssql:pymssql://rkm:UF5rrXp49IgA1$f6@msk-sql-02/RKM'
conn = 'mssql+pymssql://rkm:UF5rrXp49IgA1$f6@msk-sql-02/RKM?charset=utf8'

engine = sqlalchemy.create_engine(conn)
# engine = create_async_engine(
#     "mssql+aioodbc://rkm:UF5rrXp49IgA1$f6@msk-sql-02/RKM?"
#     "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
# )
connect = engine.connect()

inspector = sqlalchemy.inspect(engine)
print(inspector.get_table_names())
# print(inspector)

df = pd.read_sql("select * from AccrualType", connect)
print(df.head())

print(df.iloc[1:, :])
