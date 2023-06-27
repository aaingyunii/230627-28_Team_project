import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import common
import warnings

warnings.filterwarnings("ignore")

# 한글 폰트 적용
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = './NanumGothic.ttf'  # 본인의 한글 폰트 파일 경로로 변경해야 합니다.
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())


common.page_config()

df = common.get_data()

# 시도별 의료기관 수 계산
hospital_count = df['시군명'].value_counts()

tab1, tab2 = st.tabs(["Plotly", "Pyplot"])


with tab1:
    fig = go.Figure(data=[go.Bar(x=hospital_count.index, y=hospital_count.values)])
    fig.update_layout(
        xaxis=dict(
            title='시도',
            tickangle=90,
        ),
        yaxis=dict(
            title='의료기관 수',
        ),
        title='시도별 의료기관 수',
    )
    st.plotly_chart(fig,
                    use_container_width=True)

with tab2:
    plt.bar(hospital_count.index, hospital_count.values)
    plt.xlabel('시도', fontproperties=fontprop)  # 한글 폰트 설정
    plt.ylabel('의료기관 수', fontproperties=fontprop)  # 한글 폰트 설정
    plt.title('시도별 의료기관 수', fontproperties=fontprop)  # 한글 폰트 설정
    plt.xticks(rotation=90, fontproperties=fontprop)  # 한글 폰트 설정
    st.pyplot()

        
# # Streamlit 앱에 표시
# st.pyplot(plt.figure(figsize=(10, 6)))
# plt.bar(hospital_count.index, hospital_count.values)
# plt.xlabel('시도')
# plt.ylabel('의료기관 수')
# plt.title('시도별 의료기관 수')
# plt.xticks(rotation=45)
# st.pyplot()

