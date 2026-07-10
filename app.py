import streamlit as st

user_input = st.text_input("Enter your name:", "John Doe")
st.write(f"Hello, {user_input}!")