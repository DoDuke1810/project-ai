import streamlit as st

text = st.text_input('Text input', 'Default')
number = st.number_input('Number input')
textarea = st.text_area('Text area', '''Hello
COTAI''')

if st.button('OK'):
  st.write('text content:', text)
  st.write('number content:', number)
  st.write('text area content:', textarea)

check = st.checkbox('Boy')
radio = st.radio('Radio', ('Option 1', 'Option 2', 'Option 3'), horizontal=True)
if st.button('OK'):
  st.write('Check box:', check)
  st.write('Radio:', radio, type(radio))