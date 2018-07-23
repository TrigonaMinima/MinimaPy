import sqlalchemy as sqla
from sqlalchemy.sql import text


# DSN
server_name = ""
database_name = ""
driver = "SQL+Server+Native+Client+10.0"

engine_string = "mssql://%s/%s?driver=%s" % (
    server_name, database_name, driver)
print(engine_string)

# Creating engine object
engine = sqla.create_engine(engine_string)
print("DB engine object made!")

# Query structure
query_str = "SELECT * INTO %s.%s FROM %s.%s WHERE LANE = '%s.0'"


schema = "A"
query = text(query_str % (schema, 4, schema, 4)).execution_options(
    autocommit=True)
print(query)
engine.execute(query)

for lane in range(1, 4):
    query = text(query_str % (schema, lane)).execution_options(autocommit=True)
    engine.execute(query)
    print("A Lane:", lane)

print("Data uploaded to SQL.")
