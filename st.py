import streamlit as st
check = st.checkbox('Boy')
radio = st.radio('Radio', ('Option 1', 'Option 2', 'Option 3'), horizontal=True)
if st.button('OK'):
  st.write('Check box:', check)
  st.write('Radio:', radio, type(radio))
  