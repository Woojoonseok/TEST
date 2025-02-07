#%%

import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 설정
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # 필수이지만 사용되지 않음
)

# Streamlit 페이지 설정
st.title("Ollama 모델 3.1과 상호작용")
st.write("아래에 질문을 입력하고, Ollama 모델의 응답을 확인하세요.")

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:")

# 입력이 있을 때만 API 호출
if user_input:
    response = client.completions.create(
        model="llama3.1",
        prompt=user_input,
        max_tokens=150,
        temperature=0.7
    )
    
    # 응답 출력
    st.write("Ollama 모델의 응답:")
    st.write(response.choices[0].text)

# Streamlit 앱 실행: 터미널에서 streamlit run <파일명>.py 입력


# %%
