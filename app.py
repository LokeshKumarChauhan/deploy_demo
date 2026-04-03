import streamlit as st

st.title("docker Stremlit App")

name = st.text_input("Enter your name :")

if name :
    st.write(f"Hey {name}, Hope you are doing good , glad to see you here ")


print("Hello learners , welcome to revision session")