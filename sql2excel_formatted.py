import pandas as pd
import itertools as it
import sqlalchemy as sqla

from pathlib import Path


ddir = Path("")
server_name = ""
db = ""
driver = "SQL+Server+Native+Client+10.0"

engine_string = "mssql://%s/%s?driver=%s" % (server_name, db, driver)
engine = sqla.create_engine(engine_string)
print("Engine created.")

tables = []


def save_excel(data, xlfile):
    writer = pd.ExcelWriter(xlfile.as_posix(), engine='xlsxwriter')

    data.to_excel(writer, startrow=1, sheet_name='Sheet1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    for i, col in enumerate(data.columns):
        column_len = max(data[col].astype(str).str.len().max(), len(col))
        worksheet.set_column(i, i, column_len)

    writer.save()


def create_save_mapping(data, table):
    columns = ["col1", "col2", "col3"]
    data = data[columns]

    docs = data["col1"].unique()
    gls = data["col2"].unique()
    vas = data["col3"].unique()

    data = list(it.zip_longest(docs, gls, vas))
    new_df = pd.DataFrame(data, columns=columns)
    new_df["Document Name"] = table
    print("mappings done")

    f = ddir / ("mappings" + table + ".xlsx")
    new_df.to_excel(f, index=False)


def get_save_data(table):
    print("Doing table -", table)
    sql_query = f"""
        SELECT * FROM {table}
    """

    data = pd.read_sql_query(sql_query, engine)

    csv_file = ddir / (table + ".csv")
    data.to_csv(csv_file, index=False)
    print("CSV saved.")

    # excel_file = ddir / (table + ".xlsx")
    # save_excel(data, excel_file)
    # print("Excel saved.")
    # print(table, "done.\n==============")

    return data


if __name__ == '__main__':
    for table in tables:
        data = get_save_data(table)
        create_save_mapping(data, table)
