import sqlalchemy
import psycopg2

# conn = 'postgresql+psycopg2://readonly:6hajV34RTQfmxhS@dsstudents.skillbox.ru:5432/db_ds_students'
# conn = 'jdbc:sqlserver://msk-sql-02;database=RKM'
conn = 'mssql+pyodbc://rkm:UF5rrXp49IgA1$f6@msk-sql-02/RKM?trusted_connection=yes&driver=ODBC+Driver+18+for+SQL+Server'

engine = sqlalchemy.create_engine(conn)
connect = engine.connect()

inspector = sqlalchemy.inspect(engine)
print(inspector.get_table_names())
print(inspector)
