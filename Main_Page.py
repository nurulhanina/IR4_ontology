import streamlit as st
from PIL import Image


image=Image.open('Resources/Header.png')
st.image(image)
st.title("SISTEM ISTILAH DWIBAHASA")

