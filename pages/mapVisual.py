import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import common

common.page_config()

st.title("기본 지도 공간 시각화")

@st.cache_data(experimental_allow_widgets=True)
def load_map():
    df = common.get_data()

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

if __name__ == "__main__":
    load_map()