import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.image('./img/IMG_2571.jpg')
st.subheader("Simpp:) MTV🧸🎧🎸")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))


st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal_length'].sum())
cl2.write(dt['sepal_width'].sum())
cl3.write(dt['petal_length'].sum())
cl4.write(dt['petal_width'].sum())
st.write("กราฟแท่ง")
a=dt['sepal_length'].sum()
b=dt['sepal_width'].sum()
c=dt['petal_length'].sum()
d=dt['petal_width'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["sepal_length", "sepal_width", "petal_length","petal_width"])
st.bar_chart(cx)
st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['sepal_length'].mean())
cl12.write(dt['sepal_width'].mean())
cl13.write(dt['petal_length'].mean())
cl14.write(dt['petal_width'].mean())
st.write("Area_Chart")
a=dt['sepal_length'].mean()
b=dt['sepal_width'].mean()
c=dt['petal_length'].mean()
d=dt['petal_width'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["sepal_length", "sepal_width", "petal_length","petal_width"])
st.area_chart(cxx)
st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal_length'].max())
cl22.write(dt['sepal_width'].max())
cl23.write(dt['petal_length'].max())
cl24.write(dt['petal_width'].max())
import numpy as np
import matplotlib.pyplot as plt
labels = ['Men', 'Women','','']
sizes = [35,25,15,25]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)
st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['sepal_length'].min())
cl32.write(dt['sepal_width'].min())
cl33.write(dt['petal_length'].min())
cl34.write(dt['petal_width'].min())
st.write("Line_Chart")
cc=[3,8,1,10]
st.line_chart(cc)
