import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
from custom_eda_functions import *

df = sns.load_dataset('iris')
df_list = column_splitter(df)
df_num = df_list[1]
df_str = df_list[0]

st.title("title of the app")
st.markdown("Markdown Text")
st.header("quote to begin with")


selected_options = st.multiselect("Spalten", df_num.columns.tolist(), default=df_num.columns.tolist())

filtered_df = df_num[selected_options]

st.dataframe(filtered_df.head())

### streamlit run streamlit_test_app.py