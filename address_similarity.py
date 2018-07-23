import re
import difflib

import pandas as pd


pin_reg = re.compile(r"\b[0-9]{6}\b")
nonjunk_red = re.compile(r"\b\w+\b")


def read_data(sheet_name):
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    print("Read -", sheet_name)
    return df


def get_pin(x):
    # print(x)
    # print("|".join(pin_reg.findall(x)))
    return "|".join(pin_reg.findall(x))


def clean(x):
    x = nonjunk_red.findall(str(x))
    return x


def matcher(x, y):
    # x = " ".join(x)
    # y = " ".join(y)
    # print(x, y)
    return difflib.SequenceMatcher(None, x, y).ratio()


def add_new_cols(df, addr_col):
    addr_pin = addr_col[:5] + "_PIN"
    addr_words = addr_col[:5] + "_WORDS"
    addr_new = addr_col[:5] + "_NEW"

    df[addr_pin] = df[addr_col].apply(get_pin)
    df[addr_words] = df[addr_col].apply(clean).apply(sorted)
    df[addr_new] = df[addr_words].apply(lambda x: " ".join(x)).str.upper()

    return df


def add_comparison_cols(df, col1, col2, prefix=""):
    addr_pin1 = col1[:5] + "_PIN"
    addr_words1 = col1[:5] + "_WORDS"
    addr_new1 = col1[:5] + "_NEW"

    addr_pin2 = col2[:5] + "_PIN"
    addr_words2 = col2[:5] + "_WORDS"
    addr_new2 = col2[:5] + "_NEW"

    df["difflib" + prefix] = df[[addr_new1, addr_new2]].apply(
        lambda x: matcher(x[addr_new1], x[addr_new2]) * 100, axis=1)

    df["PIN MATCH" + prefix] = df[addr_pin1] == df[addr_pin2]
    # df["len_diff" +
    #     prefix] = abs(df[addr_new1].str.len() - df[addr_new2].str.len())
    # df["zscore" + prefix] = abs(df["len_diff"]-df["len_diff"].mean()
    #                             ) / df["len_diff"].std()
    df["MATCH"] = ""

    return df


def save_data(sheet_name, df):
    df.to_excel(sheet_name + ".xlsx", index=False)
    print("Saved -", sheet_name)


if __name__ == "__main__":
    input_file = ""

    addr_cols = [
    ]

    sheets = [
        "Result"
    ]
    for sheet in sheets:
        df = read_data(sheet)
        print(df.columns)
        for col in addr_cols[:1]:
            df = add_new_cols(df, col)

        df = add_comparison_cols(df, addr_cols[0], addr_cols[1])

    save_data(sheet, df)
