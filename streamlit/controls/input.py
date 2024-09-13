import streamlit as st

st.title('Input 컨트롤을 한번 사용해 봅시다.')
st.caption('https://docs.streamlit.io/develop/api-reference/widgets 이 주소를 참고하세요.')

text = st.text_input('텍스트 입력', '기본값')
if text:
    st.write(f'입력한 텍스트: {text}')

check_selected = st.checkbox('체크박스', value=False)
if check_selected:
    st.write('체크박스가 선택되었습니다.')


if st.button('버튼'):
    st.write('버튼이 눌렸습니다.')