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
if not state:
    df3=df2.copy()
else:
    df3=df2[df["State"].isin(state)]

city=st.sidebar.multiselect("Pick your City",df3["City"].unique())
# if not city:
#     df4=df3.copy()
# else:
#     df4=df3[df["City"].isin(city)]

#filter data

if not region and not state and not city:
    filtered_df=df
elif not state and not city:
    filtered_df=df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df=df[df["State"].isin(state)]
elif state and city:
    filtered_df=df3[df["State"].isin(state)&df3["City"].isin(city)]
elif region and city:
    filtered_df=df3[df["State"].isin(region)&df3["City"].isin(city)]
elif region and state:
    filtered_df=df3[df["State"].isin(region)&df3["City"].isin(state)]
elif city:
    filtered_df=df3[df3["City"].isin(city)]
else:
    filtered_df=df3[df3["Region"].isin(region)&["State"].isin(state)&df3["City"].isin(city)]
    
category_df=filtered_df.groupby(by=["Category"],as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category wise sales")
fig=px.bar(category_df,x="Category",y="Sales",text=['${:,.2f}'.format(x)for x in category_df["Sales"]],
           template="seaborn")
st.plotly_chart(fig,use_container_width=True,height=50)

with col2:
    st.subheader("Region wise Sales")
    fig=px.pie(filtered_df,values="Sales",names="Region",hole=0.5)
    fig.update_traces(text=filtered_df["Region"],textposition="outside")
    st.plotly_chart(fig,use_container_width=True)