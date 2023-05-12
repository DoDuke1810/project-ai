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
 
class = st.write('Lớp chuyên')
cola, colb, colc, cold, cole = st.columns(5)
with cola:
    math = st.checkbox('Toán')
    literature = st.checkbox('Văn')
with colb:
    ly = st.checkbox('Lý')
    hoa = st.checkbox('Hóa')
with colc:
    eng = st.checkbox('Anh')
    tin = st.checkbox('Tin')
with cold:
    su_dia = st.checkbox('Sử Địa')
    tr_n = st.checkbox('Trung Nhật')
with cole:
    th_sn = st.checkbox('TH/SN')
    diff = st.checkbox('Khác')
