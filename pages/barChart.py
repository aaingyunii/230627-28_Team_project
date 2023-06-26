import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://raw.githubusercontent.com/aaingyunii/230627-28_Team_project/main/%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80%EB%B0%8F%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EC%A7%80%EC%9B%90%EC%84%BC%ED%84%B0%ED%98%84%ED%99%A9.csv",
    encoding='cp949'
)

# # # 시도별 의료기관 수 계산
# hospital_count = df['시군명'].value_counts()

# # Streamlit 앱에 표시
# st.pyplot(plt.figure(figsize=(10, 6)))
# plt.bar(hospital_count.index, hospital_count.values)
# plt.xlabel('시도')
# plt.ylabel('의료기관 수')
# plt.title('시도별 의료기관 수')
# plt.xticks(rotation=45)
# st.pyplot()

# 시도별 의료기관 수 계산
hospital_count = df['시군명'].value_counts().reset_index()

# 바 차트 생성
fig = px.bar(hospital_count, x='시군명', y='의료기관수')

# Streamlit 앱에 표시
st.plotly_chart(fig)