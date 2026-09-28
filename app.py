import streamlit as st

st.title("My First Streamlit App by Prakhar")

st.write("Hello World!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}!")