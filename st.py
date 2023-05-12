import streamlit as st
st.title('Bé tập làm toán')
a = st.number_input('a')
radio = st.radio(label='Phép toán', options=('+', '-', 'x', ':'), horizontal=True)
b = st.number_input('b')
text = st.text_input('Nhập kết quả')
if st.button('Kiểm tra'):
    result = a + b
    if radio == '-':
        result = a - b
    elif radio == 'x':
        result = a * b
    elif radio == ':':
        result = a / b

    if result == float(text):
        st.success('Chính xác')
    else:
        st.error(f'Sai rồi, đáp số đúng là {result}')