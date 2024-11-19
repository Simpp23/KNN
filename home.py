import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.image('./img/IMG_2571.jpg')
st.subheader("Simpp:) MTV🧸🎧🎸")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))
