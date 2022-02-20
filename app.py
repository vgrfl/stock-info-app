import streamlit as st
import pandas as pd


@st.cache_data
def read_SP500():
    return pd.read_csv('SnP500.csv')

try:
    sp500_df = read_SP500()
except:
    st.exception(RuntimeError("Failed to Load the Required local Dataset"))


pg1_title = "Symbol list of S&P500 stocks"

with st.sidebar:
    #st.subheader("Page Selection")
    page = st.radio("Select a Section to view", ([pg1_title]))


if page == pg1_title:
    st.subheader("S&P 500 Stock Symbols & Company Names")
    st.dataframe(sp500_df.drop(columns="Sector"), height=600, width=500)