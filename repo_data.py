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

#date

col1,col2=st.columns((2))
df['Order Date']=pd.to_datetime(df['Order Date'])

startDate=pd.to_datetime(df['Order Date']).min()
endDate=pd.to_datetime(df['Order Date']).max()

with col1:
    date1=pd.to_datetime(st.date_input("Start date",startDate))
    
with col2:
    date2=pd.to_datetime(st.date_input("End date",endDate))
    
df=df[(df["Order Date"]>=date1)&(df["Order Date"]<=date2)].copy()

#siedbar

st.sidebar.header("Choose your filter: ")
region=st.sidebar.multiselect("Pick your Region",df["Region"].unique())

if not region:
    df2=df.copy()
else:
    df2=df[df["Region"].isin(region)]
    
state=st.sidebar.multiselect("Pick your State",df2["State"].unique())

city=st.sidebar.multiselect("Pick your City",df2["City"].unique())