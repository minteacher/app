import streamlit as st

name = "Min"

if st.button('Submit', key=1):
    st.write('Name:{}' .format(name))

if st.button('Submit', key=2):
    st.write('Full Name:{}' .format(name))