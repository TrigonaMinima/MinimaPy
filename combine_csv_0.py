import pandas as pd


files = []
alldata = []
for file in files:
    data = pd.read_csv(file, low_memory=False)
    print(len(data.columns))
    print("Data read - ", file)
    alldata.append(data)


alldata = alldata[0].append(alldata[1:])

out_file = "a.csv"
alldata.to_csv(out_file, index=False)
