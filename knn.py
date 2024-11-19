import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

st.header("Simpp:) MTV🧸🎧🎸")
st.image('./img/IMG_2571.jpg', width=250)

dt = pd.read_csv('./data/iris-3.csv')
st.subheader('ข้อมูลดิบ iris')
st.write(dt.head(10))

st.subheader('การจำแนกข้อมูลใหม่')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./img/Setosa2.jpg")

with col2:
   st.header("Verginiga")
   st.image("./img/versicolor_2.jpg")

with col3:
   st.header("Setosa")
   st.image("./img/virginica2.jpg")

html_7 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")

dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))

dt1 = dt['petal_length'].sum()
dt2 = dt['petal_width'].sum()
dt3 = dt['sepal_length'].sum()
dt4 = dt['sepal_width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
   #st.write(dt.head(10))
   st.bar_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/iris-3.csv") 
   X = dt.drop('variety', axis=1)
   y = dt.variety   
   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)   
   x_input = np.array([[pt_len, pt_wd, sp_len, sp_wd]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'Setosa':
    st.image("./img/Setosa2.jpg")
   elif out[0] == 'Versicolor':       
    st.image("./img/versicolor_2.jpg")
   else:
    st.image("./img/virginica2.jpg")
else:
    st.write("ไม่ทำนาย")