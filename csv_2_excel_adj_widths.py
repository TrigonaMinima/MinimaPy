import pandas as pd


input_file = ""
output_file = ""

data = pd.read_csv(input_file, dtype=str, low_memory=False)

writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
data.to_excel(writer, startrow=1, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
columns = len(data.columns)
column_series = pd.Series(range(columns))
column_list = column_series.tolist()

for i, col in enumerate(data.columns):
    column_len = max(a[col].astype(str).str.len().max(), len(col))
    worksheet.set_column(i, i, column_len)

writer.save()
