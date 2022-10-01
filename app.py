import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import preprocessing
import tweepy

df = pd.read_excel("fo_mktlots.xlsx")

ek_din = preprocessing.pichla_ek_din(df)

st.sidebar.title("Twitter-Sentiment-Analysis")
time = 'Previous day count'


if(time == 'Previous day count'):
    st.header("Previous day count")
    st.bar_chart(data = ek_din, x = 'keyword', y = 'count')