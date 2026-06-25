## Interactive UI

import streamlit as st
import pandas as pd

name = st.text_input("Enter your name :")

if name:
    st.write(f"hello my dear {name}")

gender= st.radio("sex",["male","female"])  

age =st.slider("select your age",0,100,25)
st.write(f"your age is {age}")

# color=st.select_slider("choose your favorite color" ,options=[
#         "red",
#         "orange",
#         "yellow",
#         "green",
#         "blue",
#         "indigo",
#         "violet",
#     ],
# )

options=["c++","java","python","html","css","javascript","ruby","c#","kotlin","C","swift","flutter","R","dart"]
lan=st.multiselect("choose your programming language:",options)
st.write(f"your choosen languages are {lan}")

data={
    "Name":["sam alto","jilie stark","murphy ruby","davel joshep"],
    "age":[26,25,27,32],
    "city":["New york","New york","los vegas","cambridge"]
}
df=pd.DataFrame(data)
st.write(df)

df.to_csv("sampleData.csv")




uploaded_file=st.file_uploader("upload the csv file ",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
