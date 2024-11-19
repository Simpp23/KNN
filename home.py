import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.image('./img/IMG_2571.jpg')
st.subheader("Simpp:) MTV🧸🎧🎸")

dt=pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.warning(dt.head(10))
