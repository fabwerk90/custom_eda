### necessary imports
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
from custom_eda_functions import *

### Global layout and headers 

st.set_page_config(layout="wide")

st.title("Exploratory Data Analysis")
st.markdown("Small application to conduct a fast EDA")

### Data ingestion

df = sns.load_dataset('iris')
df_list = column_splitter(df)
df_num = df_list[0]
df_str = df_list[1]

### Data preparation
fake = Faker()
df_str["fake_text"] = fake.text()

### Dataframe display

df_col1, df_col2 = st.columns(2)

with df_col1:
    df_col1.header("Numerical columns")
    numercial_columns = st.multiselect("Num columns", df_num.columns.tolist(), default=df_num.columns.tolist())
    filtered_df = df_num[numercial_columns]
    st.dataframe(filtered_df.head())

with df_col2:
    st.header("String columns")
    string_columns = st.multiselect("Str columns", df_str.columns.tolist(), default=df_str.columns.tolist())
    filtered_df = df_str[string_columns]
    st.dataframe(filtered_df.head())

### Distributions


############# TODOS
# 1 --- Plotting columns for numerical and string
# 2 --- Second select just for all upcoming plots
# 3 --- Distributions
# 4 --- Relationships
# 5 --- Correlations
# 6 --- Text plots
    #https://discuss.streamlit.io/t/how-to-add-wordcloud-graph-in-streamlit/818/2

# Bonus --- String "road", only if string column in dataframe



###### Run app
# streamlit run streamlit_test_app.py