# Works with MS SQL. Haven't tried with other DBs.
import os
import pandas as pd
import sqlalchemy as sqla


data_dir = ""
in_file = os.path.join(data_dir, "data.csv")

server_name = ""
database_name = ""
driver = "SQL+Server+Native+Client+10.0"

engine_string = "mssql://%s/%s?driver=%s" % (
    server_name, database_name, driver)
print(engine_string)

con = sqla.create_engine(engine_string)
print("DB connection made!")

data = pd.read_csv(in_file, dtype=str, low_memory=False)
print("Data read.")

table_name = ""
data.to_sql(
    name=table_name,
    con=con,
    schema='DBO',
    if_exists='replace',
    index=False
)
print("Data uploaded to SQL.")
