import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv(
    "https://raw.githubusercontent.com/aaingyunii/230627-28_Team_project/main/%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80%EB%B0%8F%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EC%A7%80%EC%9B%90%EC%84%BC%ED%84%B0%ED%98%84%ED%99%A9.csv",
    encoding='cp949'
)
st.bar_chart(df)
# # 시도별 의료기관 수 계산
# hospital_count = df['시군명'].value_counts()

# # 시각화
# plt.figure(figsize=(10, 6))
# hospital_count.plot(kind='bar')
# plt.xlabel('시도')
# plt.ylabel('의료기관 수')
# plt.title('시도별 의료기관 수')
# plt.xticks(rotation=45)
# plt.show()