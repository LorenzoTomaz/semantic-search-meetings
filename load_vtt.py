import re
import webvtt
import pandas as pd
import numpy as np


def load_vtt_datasets():
    files = [
        "data/text/zoomGroupStats/meeting001_transcript.vtt",
        "data/text/zoomGroupStats/meeting002_transcript.vtt",
        "data/text/zoomGroupStats/meeting003_transcript.vtt",
    ]

    get_name = (
        lambda caption: re.search("[A-Za-z0-9\s]+:", caption.text)
        .group()
        .replace(":", "")
        if re.search("[A-Za-z0-9\s]+:", caption.text)
        else None
    )
    remove_name = (
        lambda caption: caption.text.replace(
            re.search("[A-Za-z0-9\s]+:", caption.text).group(), ""
        ).strip()
        if re.search("[A-Za-z0-9\s]+:", caption.text)
        else caption.text
    )

    data = [
        {
            "start": caption.start,
            "end": caption.end,
            "text": remove_name(caption),
            "id": caption.start + "->" + caption.end,
            "user": get_name(caption),
        }
        for file in files
        for caption in webvtt.read(file)
    ]
    df = pd.DataFrame(data, columns=["text", "end", "start", "user"])
    df.replace("", np.nan, inplace=True)
    df.dropna(inplace=True)
    df = df.reset_index()
    df["index_column"] = df.index
    print(df.head())
    df.to_csv("conversation_vtt.csv", index=False)


if __name__ == "__main__":
    load_vtt_datasets()
