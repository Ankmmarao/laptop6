import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
import plotly.express as px
from PIL import Image
logo = Image.open('C:\Users\India\Pictures\durgamma.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 

st.set_page_config(page_title="Laptap  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6162-v.Praneeth", "21A21A6138-M.Ankammarao", "21A21A6129-k.reshi charan","21A21A6141-murali","21A21A6124-Gopi","21A21A6135-Dinesh"]
st.title("Exploratory Data Analysis on laptap Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a  laptap Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    pd.DataFrame(data)
    st.title("laptap Data Analysis")
if st.checkbox("Get the head of the data"):
    st.write(data.head())
if st.checkbox("Get the mean of the all the laptaps"):
    st.write(data['price'].mean())
if st.checkbox("Get the maimum price of the laptap"):
    st.write(data['price'].max())
    
if st.checkbox("Get the minimum price of the laptap"):
     st.write(data['price'].min())
if st.checkbox("Get the columns of the Dataset"):
    st.write(data.columns)
if st.checkbox("Get the shape of the Dataset"):
    st.write(data.shape)
if st.checkbox("Get the unique values of the DataSet"):
    st.write(data['name'].unique())
if st.checkbox("Get the null value of the dataset"):
    st.write(data.isnull().sum())
if st.checkbox("Get the None_null value of the dataset"):
    st.write(data.notnull().sum())
if st.checkbox("Get the index of the Dataset"):
    st.write(data.index)
if st.checkbox("Rename the price(in Rs.) to the price"):
    A=data.rename(columns={'price':'price'},inplace=True)
    st.write(A)
    st.write(data.head())
if st.checkbox("The Graphical Represantatin of the price vs Laptop type"):
    a=st.write(pd.DataFrame(data['price']))
    b=st.write(pd.DataFrame(data['name']))
    st.write(plt.scatter(a,b))
if st.checkbox("The Graphical Represantation of the price"):
    v=st.write(pd.DataFrame(data['price']))
    st.write(hist(v))
if st.checkbox("Select type of the processor"):
    st.checkbox( "Get the size of the DataSet:")
    st.write(data.size)
if st.checkbox("Get the Indexes of the DataSet:"):
    st.write(data.index)
if st.checkbox("Get the Shape of the DataSet:"):
    st.write(data.shape)
if st.checkbox("Get the Unique processors of the Laptop:"):
    st.write(data['processor'].unique())
if st.checkbox("Get the Unique of the Laptops:"):
    st.write(data['name'].unique())
if st.checkbox("Get the Unique of the Operating Syatem:"):
    st.write(data['os'].unique())
#now the statistical part is there
if st.checkbox("Get the Average price of the laptop:"):
    st.write(data['price'].sum())
if st.checkbox("Get the mac price of the laptop:"):
    st.write(data['price'].max())
if st.checkbox("Get minimum price of the laptop price:"):
    st.write(data['price'].min())
if st.checkbox("By using the Descibe function Analysize price of the Each laptop:"):
    st.write(data['price'].describe())
if st.checkbox("Get the total no.of Laptops in the Dataset:"):
    st.write(data['price'].count())
if st.checkbox("Get the all the unique processor:"):
    st.write(pd.DataFrame(data['processor']))

        
