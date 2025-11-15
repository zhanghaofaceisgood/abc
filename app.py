import streamlit as st

st.title('˗ˏˋ ꒰ ♡ ꒱ ˎˊ˗')

name = st.text_input('이름')

if st.button('안녕하세요'):
    st.write(f'안녕하세요, {name}님 ! !')

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF4F7;
        background-image: radial-gradient(#FADCE2 8%, transparent 8%);
        background-size: 40px 40px; /* 점 간격 조절 */
    }
    </style>
    """,
    unsafe_allow_html=True
)
