import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/aaingyunii/230627-28_Team_project/main/%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80%EB%B0%8F%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EC%A7%80%EC%9B%90%EC%84%BC%ED%84%B0%ED%98%84%ED%99%A9.csv",
    encoding='cp949'
)

# 지도 초기화
m = folium.Map(location=[37.5502, 126.982], zoom_start=8)  # 초기 위치와 줌 레벨 설정
                                                            # 초기 위치 -> 서울의 중심 location=[37.5502, 126.982]
# 데이터프레임 순회하며 위치 표시
for index, row in df.iterrows():
    if pd.notnull(row['위도']) and pd.notnull(row['경도']): # 각 행의 위도와 경도 값이 유효한 경우에만 위치를 표시합니다. (pd.notnull() 함수를 사용하여 유효성을 확인합니다.)
        folium.Marker(location=[row['위도'], row['경도']]).add_to(m) # 위치를 표시하기 위해 folium.Marker를 생성하고 지도에 추가합니다.

# 지도 출력
st_folium(m)