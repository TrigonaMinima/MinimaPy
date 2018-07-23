import os
import pandas as pd


columns = ["col1", "col2"]
delimiter = "|"
input_dir = "."
output_dir = ""
csv_flag = 1
headers = None

final_file_name = "a.csv"

data = []
count = 0

for file in os.listdir(input_dir):
    # file_path = os.path.join(input_dir, file)
    # print(file)
    file_path = file
    if csv_flag and file_path.endswith(".csv"):
        count += 1
        print(count, ".", file_path, end=" - ")
        try:
            if headers is None:
                table = pd.read_csv(file_path, header=headers)
                table.columns = columns
            else:
                table = pd.read_csv(file_path)
        except UnicodeDecodeError:
            if headers is None:
                table = pd.read_csv(
                    file_path, encoding="cp1252", header=headers)
                table.columns = columns
            else:
                table = pd.read_csv(file_path, encoding="cp1252")

        table["File"] = file_path
        print(table.shape)
        data.append(table)
    # elif not csv_flag and file_path.endswith(".txt"):
    elif not csv_flag and not file_path.endswith(".py"):
        count += 1
        print(count, ".", file_path, end=" - ")
        try:
            if headers is None:
                table = pd.read_table(
                    file_path, delimiter=delimiter, header=headers)
                table.columns = columns
            else:
                table = pd.read_table(file_path, delimiter=delimiter)
        except UnicodeDecodeError:
            if headers is None:
                table = pd.read_table(
                    file_path, delimiter=delimiter, encoding="cp1252", header=headers)
                table.columns = columns
            else:
                table = pd.read_table(
                    file_path, delimiter=delimiter, encoding="cp1252")

        table["File"] = file_path
        print(table.shape)
        data.append(table)


data = pd.concat(data)
data.to_csv(final_file_name, index=False, encoding="utf8")
