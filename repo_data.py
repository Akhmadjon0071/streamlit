import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Data Visualization",page_icon="📈",layout="wide")
st.title(":bar_chart: Data Visualization EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl=st.file_uploader(":file_folder Upload a file",type=(["csv","txt","xlxs","xls"]))
if fl is not None:
    filename=fl.name
    st.write(filename)
    df=pd.read_csv(filename,encoding="UTF-8")
else:
    os.chdir(r"/home/akhmadjon/Documents/github")
df=pd.read_csv("sample.csv", encoding="UTF-8")

