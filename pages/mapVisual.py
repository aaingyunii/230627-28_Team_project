import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/aaingyunii/230627-28_Team_project/main/%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80%EB%B0%8F%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EC%A7%80%EC%9B%90%EC%84%BC%ED%84%B0%ED%98%84%ED%99%A9.csv",
    encoding='cp949'
)

# 서울-경기도 부근 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# 데이터프레임 순회하며 위치 표시
for index, row in df.iterrows():
    if pd.notnull(row['위도']) and pd.notnull(row['경도']):
        lat, lon = row['위도'], row['경도']
        # 서울-경기도 부근인 경우에만 표시
        if 37.0 <= lat <= 38.5 and 126.0 <= lon <= 127.5:
            folium.Marker(location=[lat, lon]).add_to(m)

# 지도 출력
st_folium(m)