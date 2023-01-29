import re
import pandas as pd
import numpy as np


def generates_conversation_dataset():
    data = []
    files = [
        "data/text/conversation-meetings-kaggle/conversation1.txt",
        "data/text/conversation-meetings-kaggle/conversation2.txt",
        "data/text/conversation-meetings-kaggle/conversation3.txt",
    ]
    get_name = (
        lambda text: re.search("[A-Za-z0-9\s]+:", text).group().replace(":", "")
        if re.search("[A-Za-z0-9\s]+:", text)
        else None
    )
    remove_name = (
        lambda text: text.replace(
            re.search("[A-Za-z0-9\s]+:", text).group(), ""
        ).strip()
        if re.search("[A-Za-z0-9\s]+:", text)
        else text
    )
    for file in files:
        print(file)
        with open(
            file,
            "r",
            encoding="ISO 8859-1",
        ) as conv:
            conv_text = conv.read()
            items = [
                {"user": get_name(el), "text": remove_name(el)}
                for el in conv_text.split("\n")
            ]

            data = [*data, *items]

    df = pd.DataFrame(data, columns=["text", "user"])
    df.replace("", np.nan, inplace=True)
    df.dropna(inplace=True)
    df = df.reset_index()
    df["index_column"] = df.index
    print(df.head())
    df.to_csv("conversation.csv", index=False)


if __name__ == "__main__":
    generates_conversation_dataset()
