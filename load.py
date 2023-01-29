import pandas as pd
import numpy as np


def generates_conversation_dataset():
    data = []
    files = [
        "data/text/conversation-meetings-kaggle/conversation1.txt",
        "data/text/conversation-meetings-kaggle/conversation2.txt",
        "data/text/conversation-meetings-kaggle/conversation3.txt",
    ]

    for file in files:
        print(file)
        with open(
            file,
            "r",
            encoding="ISO 8859-1",
        ) as conv:
            conv_text = conv.read()
            data = [*data, *conv_text.split("\n")]

    df = pd.DataFrame(data, columns=["text"])
    df.replace("", np.nan, inplace=True)
    df.dropna(inplace=True)
    df = df.reset_index()
    df["index_column"] = df.index
    print(df.head())
    df.to_csv("conversation.csv", index=False)


if __name__ == "__main__":
    generates_conversation_dataset()
