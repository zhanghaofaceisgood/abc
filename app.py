import streamlit as st

st.title('˗ˏˋ ꒰ ♡ ꒱ ˎˊ˗')

name = st.text_input('이름')

if st.button('안녕하세요'):
    st.write(f'안녕하세요, {name}님 ! !')

st.markdown(
    """
    <style>

    /* 전체 배경색 - 아주 연한 핑크 */
    body {
        background-color: #FDF0F3;
    }

    /* Streamlit 앱의 메인 컨테이너 배경색도 맞춰주기 */
    .main {
        background-color: #FDF0F3;
    }

    /* 제목(H1) 스타일 */
    h1 {
        color: #E58CA2;        /* 배경보다 조금 더 진한 웜한 핑크 */
        font-weight: 800;      /* 굵게 */
        font-size: 2.4rem;     /* 크게 */
    }

    /* h2, h3 같은 다른 헤더도 비슷하게 */
    h2, h3 {
        color: #E58CA2;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)
