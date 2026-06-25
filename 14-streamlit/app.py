import streamlit as st
import pandas as pd 
import numpy as np

## title of the application 

st.title("hello sudhanshu")

##  display a simple text

st.write("this is a simple text")

## streamlit ka prayog with panda 

df=pd.DataFrame({
    'first column ':[1,2,3,4,5],
    'second column':["sudhanshu" , "priya" , "dev" ,"akanksha" ,"sam"]

})
st.write(df)

## creating a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.area_chart(chart_data)
st.line_chart(chart_data)
st.bar_chart(chart_data)