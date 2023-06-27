import streamlit as st
import common 

common.page_config()

st.title("경기도 병원 데이터 시각화")
st.caption("""
"응급의료기관 및 응급의료지원센터 현황" (hospital) : 해당 데이터셋은 경기데이터드림 사이트에서 발췌한 데이터로,
경기도 내 응급의료기관 및 응급의료지원센터 현황을 알 수 있고, 각 병원들의 위도, 경도, 주소지 등의 데이터들이 포함되어있습니다.
""")
st.image("img/hospital.png")