import streamlit as st
import main

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title('회의록 작성 서비스')

# 녹음 상태를 저장할 세션 상태 변수 설정
if 'recording' not in st.session_state:
    st.session_state.recording = False

# 녹음 결과를 저장할 세션 상태 변수 설정
if 'transcript' not in st.session_state:
    st.session_state.transcript = ""

# 녹음 함수 시작 (예제)
def start_recording():
    
    # 여기에 녹음 시작 코드를 작성하세요.
    st.session_state.recording = True
    main.input_microphone()

# 녹음 함수 종료 (예제)
def stop_recording():
    transcript = main.printR()
    # 여기에 녹음 종료 코드를 작성하세요.
    st.session_state.recording = False
    st.session_state.transcript = transcript

# 버튼 클릭 이벤트 처리
if st.button('시작하기' if not st.session_state.recording else '녹음중..'):
    if st.session_state.recording:
        stop_recording()
    else:
        start_recording()

# 녹음 중일 때 빨간 점 표시
if st.session_state.recording:
    st.markdown("<div style='text-align: center; font-size: 50px; color: red;'>●</div>", unsafe_allow_html=True)

# 녹음 결과 표시
if st.session_state.transcript:
    st.subheader("녹음 결과")
    st.text(st.session_state.transcript)
