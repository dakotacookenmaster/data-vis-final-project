import streamlit as st
import pandas as pd
import os

file_dir = "./american-news-articles/crawl_json"
filenames = os.listdir(file_dir)
dataframes = []

for file in filenames[0:100]:
    new_dataframe = pd.DataFrame(pd.read_json(f"{file_dir}/{filenames[0]}"))
    new_dataframe.columns = [f"{column}_{file}" for column in new_dataframe.columns]
    dataframes.append(new_dataframe)


result = pd.concat(dataframes, axis=1)
st.write("Publications by Source Domain")
st.bar_chart(result.loc["source_domain"].value_counts())

