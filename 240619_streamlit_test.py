# 실행은 터미널에서 streamlit run 240619_streamlit_test.py

import streamlit as st
from PIL import Image   #이미지를 불러올때 사용

# st.title("안녕하세요!")
# st.header("손상범")

#사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value="",max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력", value="",type="password")

if user_id=='ssb2001' and user_password == "1234" :
        
    st.sidebar.header("그림 목록")
    sel_options=["","진주 귀걸이를 한 소녀","별이 빛난는 밤","절규","생명의 나무","월하정인"]
    user_opt = st.sidebar.selectbox('좋아하는 작품은? ', sel_options, index=0)
    st.sidebar.write("***선택한 그림은 ", user_opt)

    #메인 화면(오른쪽 화면)
    st.subheader("메인 화면")
    image_files=["welcome.jpg","girl.png","star.png","cray.png","tree.jpg","moon.png"]
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f'240619_img/{img_file}')
    st.image(img_local, caption=user_opt)
