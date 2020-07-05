import sqlalchemy as sqla
import pandas as pd


server_name = ""
database_name = ""
driver = "SQL+Server+Native+Client+10.0"

engine_string = "mssql://%s/%s?driver=%s" % (
    server_name, database_name, driver)
print(engine_string)

con = sqla.create_engine(engine_string)


sql_query = """
"""

out_file = ""
data = pd.read_sql_query(sql_query, con)
data.to_excel(out_file, index=False)
