import pandas as pd


files = [
]
split_rows = 800000


for file in files:
    print(file)
    data = pd.read_csv(file, low_memory=False)

    rows = data.shape[0]
    splits = rows // split_rows

    dfs = []
    for i in range(splits):
        dfs.append(data.iloc[i * split_rows:(i + 1) * split_rows, :])
    dfs.append(data.iloc[(splits) * split_rows:, :])

    for i, df in enumerate(dfs):
        outfile = file.replace(".", f"{i}.")
        df.to_csv(outfile, index=False)
        print("\t", outfile)
