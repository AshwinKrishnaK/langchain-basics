import streamlit as st

st.title("Streamlit Text input")

st.write("Age Slider")
age=st.slider("select your age:",0,100,25)

name=st.text_input("Enter your name: ")

if name:
    st.write(f"Hello {name}")