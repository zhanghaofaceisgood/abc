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

    """
    <style>
    /* 배경색 + 도트 */
    .stApp {
        background-color: #FFF4F7;
        background-image: radial-gradient(#FADCE2 8%, transparent 8%);
        background-size: 40px 40px;
    }

    /* 제목 스타일 */
    h1, h2, h3, .stMarkdown h1 {
        font-weight: 700; /* 굵게 */
        color: #E8A9B5;   /* 부드럽게 대비되는 핑크 */
        text-shadow: 0px 0px 6px rgba(255, 255, 255, 0.7); /* 은근한 그림자 */
    }
    </style>
    """,
    unsafe_allow_html=True
)
