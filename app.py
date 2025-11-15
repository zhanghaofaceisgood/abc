import streamlit as st

st.title('⋅˚₊‧ 𐙚 ‧₊˚ ⋅')

name = st.text_input('이름을 입력하세요:')

if st.button('안녕하세요'):
    st.write(f'안녕하세요, {name}님!')
