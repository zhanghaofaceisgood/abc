import streamlit as st

st.title('‧₊˚⋅♡⋅˚₊‧')

name = st.text_input('이름')

if st.button('안녕하세요'):
    st.write(f'안녕하세요, {name}님 ! !')

st.markdown(
    """
    <style>
        /* 전체 배경색 변경 */
        .stApp {
            background-color: #M20; /* 연한 웜 핑크 */
        }
    </style>
    """,
    unsafe_allow_html=True
)
