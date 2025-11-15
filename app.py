import streamlit as st

st.title('‧₊˚⋅♡⋅˚₊‧')

name = st.text_input('이름')

if st.button('안녕하세요'):
    st.write(f'안녕하세요, {name}님 ! !')
