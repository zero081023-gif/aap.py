import streamlit as st
import math

def fatigue(t):
    return 58 * math.exp(-0.344 * t) + 5.4

st.title("사회적 피로도 계산기")
st.write("대화 후 시간이 지날수록 피로도가 어떻게 감소하는지 계산합니다.")

t = st.number_input("시간 t (단위: 시간)", min_value=0.0, step=0.5)

if t >= 0:
    st.write(f"📉 예상 피로도: **{fatigue(t):.2f} 점**")
Add app.py
