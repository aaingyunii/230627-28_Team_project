import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    return pd.read_csv("./hospital.csv",encoding="cp949")

def page_config():
    st.set_page_config(
        page_title="경기도 병원 데이터 시각화",
        page_icon="🏥",
    )