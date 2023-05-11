import streamlit as st

text = st.text_input('Text input', 'Default')
number = st.number_input('Number input')
textarea = st.text_area('Text area', '''Hello
COTAI''')

if st.button('OK'):
  st.write('text content:', text)
  st.write('number content:', number)
  st.write('text area content:', textarea)