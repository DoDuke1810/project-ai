import streamlit as st

option = st.selectbox('Selectbox', ('select 1', 'select 2', 'select 3'))
options = st.multiselect('Multiselect', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
slider = st.slider('Slider', 0, 130, 25)
day = st.select_slider('Select slider', options=['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'], value=['Monday', 'Wednesday'])

if st.button('Click'):
    st.write('select box:', option)
    st.write('multiselect:', options, type(options))
    st.write('slider:', slider)
    st.write('select slider:', day)