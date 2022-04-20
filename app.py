import pandas as pd
import streamlit as st

text = st.text_area(
    "ここにいれてね"
)

# https://share.streamlit.io/streamlit/release-demos/0.88/0.88/streamlit_app.py
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


def main():
    is_sample = False
    list_sample = []

    is_log = False
    list_log = []

    lines = text.split("\n")

    for line in lines:
        if line == "Measurement samples:":
            is_sample = True
            continue
        elif line == "Measurement logs:":
            is_log = True
            continue

        if is_sample:
            if line == "":
                is_sample = False
                continue

            list_sample.append(line.split())
        elif is_log:
            if line == "":
                is_log = False
                continue

            list_log.append(line.split())
    print(list_log, list_sample)
    df_sample = pd.DataFrame(
        list_sample[1:],
        columns=list_sample[0]
    )

    print(df_sample)

    df_log = pd.DataFrame(
        list_log[1:],
        columns=list_log[0]
    )
    print(df_log)

    st.dataframe(df_sample)
    csv = convert_df(df_sample)
    # df_sample.to_csv("measurement_sample.csv")
    st.download_button(
        "download",
        csv,
        "measurement_sample.csv",
        "text/csv",
        key="browser-data"
    )

    st.dataframe(df_log)
    csv = convert_df(df_log)
    # df_sample.to_csv("measurement_sample.csv")
    st.download_button(
        "download",
        csv,
        "measurement_sample.csv",
        "text/csv",
        key="browser-data"
    )



if st.button("RUN"):
    main()
