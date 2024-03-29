import sqlalchemy
import psycopg2

conn = 'postgresql+psycopg2://readonly:6hajV34RTQfmxhS@dsstudents.skillbox.ru:5432/db_ds_students'

engine = sqlalchemy.create_engine(conn)
connect = engine.connect()

inspector = sqlalchemy.inspect(engine)
print(inspector.get_table_names())
print(inspector)
