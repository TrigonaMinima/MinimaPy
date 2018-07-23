# Extended Data Dictionary
import os
import pandas as pd


output_dir = ""
data_file = ""
edd_file = ""


def get_edd(df):
    edd = {
        "Col Name": [],
        "Unique Count": [],
        "Populated Rows": [],
        "Total row count": []
    }

    cols = df.columns
    for col in cols:
        temp_col = df[col].str.strip()
        temp_col = temp_col.apply(lambda x: x if x else pd.np.nan)
        unique_col_data = temp_col.unique()

        edd["Col Name"].append(col)
        edd["Unique Count"].append(len(unique_col_data))
        edd["Populated Rows"].append(len(temp_col.dropna()))
        edd["Total row count"].append(df.shape[0])

    return pd.DataFrame(edd)


data = pd.read_csv(data_file, dtype=str, low_memory=False)
print(data_file, "- read!")

edd = get_edd(data)
edd.to_csv(os.path.join(output_dir, edd_file), index=False)
print(edd_file, "- Summary saved!")
