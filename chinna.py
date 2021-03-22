import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
username=st.text_input  ("username")
upload=st.file_uploader("uploadfile",type=['csv'])
button=st.button("submit")
if button==True:
        df=pd.read_csv(upload)
        st.write(df.head())
        fig = plt.figure()
        my = fig.add_subplot(1,1,1)
        my.scatter(df["sepal.length"],df["petal.length"],)
        my.set_xlabel("sepal.length")
        my.set_ylabel("petal.length")
        st.write(fig)
