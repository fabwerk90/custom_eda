import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from custom_eda_functions import *

#st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

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

col1.header("Distributions")
col1.pyplot(numerical_distributions(filtered_df))
col2.header("Relationships")
col2.pyplot(relationships(filtered_df))


st.pyplot(text_eda(df_str, "species"))
#st.pyplot(wordcloud)

### streamlit run streamlit_test_app.py