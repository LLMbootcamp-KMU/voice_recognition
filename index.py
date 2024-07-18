import streamlit as st
import speech_recognition as sr
from threading import Thread

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 제목 설정
st.title('회의록 작성 서비스')

# 녹음 상태를 저장할 세션 상태 변수 설정
if 'recording' not in st.session_state:
    st.session_state.recording = False

# 음성 인식을 처리하는 함수
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("말하세요...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        st.write("인식된 텍스트: " + text)
        print("인식된 텍스트:")
    except sr.UnknownValueError:
        st.write("Google Web Speech API가 당신의 말을 이해하지 못했습니다.")
    except sr.RequestError as e:
        st.write(f"Google Web Speech API 서비스에 문제가 발생했습니다; {e}")

# 버튼 클릭 이벤트 처리
if st.button("음성 인식 시작/종료"):
    st.session_state.recording = not st.session_state.recording
    if st.session_state.recording:
        st.write("음성 인식을 시작합니다...")
        # 음성 인식을 별도의 스레드에서 실행
        recognize_speech()
    else:
        st.write("음성 인식을 종료합니다...")

# 녹음 중일 때 빨간 점 표시
if st.session_state.recording:
    st.markdown("<div style='text-align: center; font-size: 50px; color: red;'>●</div>", unsafe_allow_html=True)
