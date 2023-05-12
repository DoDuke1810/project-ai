import streamlit as st
col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.write('Giới tính')
    male = st.checkbox('Nam')
    female = st.checkbox('Nữ')

with col2: 
    radio = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', "Lớp 12"), horizontal=True)

with col3: 
    AI_class = st.selectbox('Phòng', ('Tất cả','A114', 'A115'))

with col4: 
    times = st.multiselect('Buổi', ['Sáng','Chiều'])
  
