import streamlit as st
from datetime import datetime

from components.calculator import calculator_component
from modes.practice import practice_mode
from modes.learn import learn_mode
from modes.quiz import quiz_mode
from modes.collaboration import collaboration_mode

st.set_page_config(page_title="AI Math Platform", layout="wide")

if "registered" not in st.session_state:
    st.session_state.registered = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.registered:
    st.title("AI Math Platform")
    st.write("Please register to use the platform.")
    name = st.text_input("Your name:", key="register_name")
    if st.button("Register", key="register_btn") and name.strip():
        st.session_state.user_name = name.strip()
        st.session_state.registration_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.registered = True
        st.rerun()
    st.stop()

st.sidebar.markdown(f"**User:** {st.session_state.user_name}")

calculator_component()

mode = st.sidebar.radio(
    "Choose Mode",
    ["Practice", "Learn", "Quiz Challenge", "Collaboration"]
)

if mode == "Practice":
    practice_mode()
elif mode == "Learn":
    learn_mode()
elif mode == "Quiz Challenge":
    quiz_mode()
elif mode == "Collaboration":
    collaboration_mode()
