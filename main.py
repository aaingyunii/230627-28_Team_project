import pandas as pd
import folium
import streamlit as st

# Read the CSV file into a DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/aaingyunii/practice02/main/%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B4%80%EB%B0%8F%EC%9D%91%EA%B8%89%EC%9D%98%EB%A3%8C%EC%A7%80%EC%9B%90%EC%84%BC%ED%84%B0%ED%98%84%ED%99%A9.csv", encoding='cp949')

# Fill missing values in selected columns
df['응급의료지원센터여부'] = df['응급의료지원센터여부'].fillna('0')
df['전문응급의료센터여부'] = df['전문응급의료센터여부'].fillna('0')
df['전문응급센터전문분야'] = df['전문응급센터전문분야'].fillna('0')
df['권역외상센터여부'] = df['권역외상센터여부'].fillna('0')
df['지역외상센터여부'] = df['지역외상센터여부'].fillna('0')
df['소재지도로명주소'] = df['소재지도로명주소'].fillna('0')
df['소재지지번주소'] = df['소재지지번주소'].fillna('0')
df['소재지우편번호'] = df['소재지우편번호'].fillna('0')
df['위도'] = df['위도'].fillna('0')
df['경도'] = df['경도'].fillna('0')

# Create a map centered on South Korea
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# Iterate over each hospital row and add a marker to the map
for index, row in df.iterrows():
    lat = row['위도']
    lon = row['경도']
    name = row['병원명/센터명']
    address = row['소재지지번주소']
    marker = folium.Marker([lat, lon], popup=f"{name}<br>{address}")
    marker.add_to(m)

# Convert the folium map to HTML
m.save("map.html")

# Use Streamlit to display the map
st.markdown('<h1>Hospital Map</h1>', unsafe_allow_html=True)
st.markdown('<iframe src="map.html" width="1000" height="500"></iframe>', unsafe_allow_html=True)
