import streamlit as st
col1, col2, col3, col4 = st.columns(3)

with col1:
    st.subheader("A cat")

with col2:
    st.header("A dog")

with col3:
    st.header("An owl")

st.text('This text is outside of column')