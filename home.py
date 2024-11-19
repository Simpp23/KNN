import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.image('./img/IMG_2571.jpg')
st.subheader("Nattawat MTV🧸🎧🎸")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.warning(dt.head(10))
