import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import bar_chart_race as bcr
from plotly.subplots import make_subplots


st.title ('pokemon Data Analysis and Visualization')
st.markdown("Welcome to our pokemon Data Analysis and Visualization Dashboard!progress with real-time data updates, interactive visualizations, and comparative analysis. Gain global and regional insights, customize charts and graphs, and access predictive analytics. Stay informed, stay safe!")


#load dataset
pk = pd.read_csv(r"C:\Users\91902\Documents\my course\pokemon.csv")


fig1 = px.scatter(pk, x='pokemon_Name', y='Sp. Atk',color='pokemon_Name')
st.plotly_chart(fig1)

fig2 = px.bar(pk, x='pokemon_Name', y='Sp. Atk',color='pokemon_Name',title='Pokemon dataset',
       labels={'pokemon_Name:Catagory','pokemon_Name'},height=1000,width=1200,template='plotly_dark')
st.plotly_chart(fig2)