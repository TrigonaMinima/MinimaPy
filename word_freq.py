import pandas as pd

# List of strings
items = []


def remove_junk(item):
    junk_str = ":_()-,+"
    for i in junk_str:
        item = item.replace(i, " ")
    return item


items = pd.Series(items)
items = items.apply(lambda x: remove_junk(x))
items = items.str.strip().str.split()

words = []
for item in items.values:
    words += item

words = pd.Series(words)
words = words.str.lower()

words_df = pd.DataFrame({
                        'words': words.value_counts().index,
                        'freq': words.value_counts()
                        })

words_df.to_csv("freq.csv", index=False, encoding="utf8")
