#
# Convert most files with wrong encoding (mix of utf-8 and latin-1) into utf-8 encoded csvs
#

import pandas as pd
import io


file_name = "RSEG_for_edd_v1.csv"
output_file = file_name.replace(".csv", "_final.csv")
delimiter = b","


def read_data(file_name):
    data = []
    with open(file_name, "rb") as f:
        data = f.readlines()

    data = [row.strip(b"\n").strip(b"\r") for row in data]
    return data


def encode_in_unicode(data, delimiter):
    for index, row in enumerate(data):
        temp_row = row.split(delimiter)
        # print(len(temp_row))

        for col_index, col in enumerate(temp_row):
            # print(len(temp_row[col_index]))
            try:
                __ = temp_row[col_index].decode("utf-8")
            except UnicodeDecodeError:
                print(1, end="-")
                temp_row[col_index] = temp_row[col_index].decode(
                    "latin-1").encode("utf-8")
            # print(len(temp_row[col_index]))
            # print()

        data[index] = delimiter.join(temp_row).decode("utf-8")

    data = "\n".join(data)
    return data


def to_df(data):
    data = data.replace('\ufeff', "")
    data = pd.read_table(io.StringIO(data))
    # data = pd.DataFrame(data[1:], columns=data[0])
    # data = pd
    print(data.head())
    return data


if __name__ == "__main__":
    # file_name = "a.txt"
    data = read_data(file_name)
    data = encode_in_unicode(data, delimiter)
    data = to_df(data)
    data.to_csv(output_file, index=False, encoding="utf-8")
